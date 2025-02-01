from models import User, Resume, Session
from datetime import datetime

def test_create_user(test_db):
    """Test creating a user"""
    user = User(user_name="testuser", email="test@example.com", password="securepassword")
    test_db.add(user)
    test_db.commit()

    retrieved_user = test_db.query(User).filter_by(user_name="testuser").first()
    assert retrieved_user is not None
    assert retrieved_user.email == "test@example.com"

def test_create_resume(test_db):
    """Test adding a resume for a user"""
    user = User(user_name="testuser", email="test@example.com", password="securepassword")
    test_db.add(user)
    test_db.commit()

    resume = Resume(user_name="testuser", file_path="/path/to/resume.pdf", uploaded_at=datetime.utcnow())
    test_db.add(resume)
    test_db.commit()

    retrieved_resume = test_db.query(Resume).filter_by(user_name="testuser").first()
    assert retrieved_resume is not None
    assert retrieved_resume.file_path == "/path/to/resume.pdf"

def test_create_session(test_db):
    """Test creating a session entry"""
    user = User(user_name="testuser", email="test@example.com", password="securepassword")
    test_db.add(user)
    test_db.commit()

    resume = Resume(user_name="testuser", file_path="/path/to/resume.pdf", uploaded_at=datetime.utcnow())
    test_db.add(resume)
    test_db.commit()

    session_entry = Session(
        user_name="testuser", resume_id=resume.resume_id,
        job_title="Software Engineer", seniority_level="Mid", alignment_percentage=85.5
    )
    test_db.add(session_entry)
    test_db.commit()

    retrieved_session = test_db.query(Session).filter_by(user_name="testuser").first()
    assert retrieved_session is not None
    assert retrieved_session.job_title == "Software Engineer"
