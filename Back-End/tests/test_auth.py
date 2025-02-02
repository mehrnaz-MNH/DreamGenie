import pytest
from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import get_db, Base
import models

# Create a test database (SQLite in-memory for simplicity)
TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override get_db dependency to use test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Apply dependency override
app.dependency_overrides[get_db] = override_get_db

# Create tables for test database
Base.metadata.create_all(bind=engine)

# Test client
client = TestClient(app)


@pytest.fixture
def test_user():
    """Registers a test user before login tests."""
    user_data = {
        "user_name": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 201
    return user_data


def test_register_user():
    """Test user registration route."""
    user_data = {
        "user_name": "newuser",
        "email": "newuser@example.com",
        "password": "securepassword"
    }
    response = client.post("/register", json=user_data)
    assert response.status_code == 201
    assert response.json()["user_name"] == "newuser"


def test_login_user(test_user):
    """Test user login route."""
    login_data = {
        "username": test_user["user_name"],
        "password": test_user["password"]
    }
    response = client.post("/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_invalid_user():
    """Test login with incorrect credentials."""
    login_data = {
        "username": "invaliduser",
        "password": "wrongpassword"
    }
    response = client.post("/login", data=login_data)
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect username or password, please try again!"


