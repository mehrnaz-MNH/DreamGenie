#Making connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



DB_URL = 'sqlite:///./dreamGenie.db'

engine = create_engine()
