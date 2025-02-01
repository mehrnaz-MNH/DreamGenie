#Making connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base


DB_URL = 'sqlite:///./dreamGenie.db'

# for testing the database
#DB_URL = 'sqlite:///:memory:'

engine = create_engine(DB_URL, connect_args={"check_same_thread" : False})

sessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)

Base = declarative_base()


