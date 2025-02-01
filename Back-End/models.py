# table
from database import Base
from sqlalchemy import Column, ForeignKey , Integer , String , Float , DateTime , PrimaryKeyConstraint
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    user_name = Column(String , primary_key=True , nullable=False , unique=True , index=True)
    email = Column(String , nullable=False , unique=True , index=True  )
    password = Column(String , nullable=False , index=True  )

    resume = relationship("Resume", back_populates="user")
    session = relationship("Session", back_populates="user")



class Resume(Base):
    __tablename__ = "resumes"
    resume_id = Column(Integer, primary_key=True, autoincrement=True , index=True)
    user_name = Column(String , ForeignKey("users.user_name") ,  nullable=False)
    file_path = Column(String , nullable = False )
    uploaded_at = Column(DateTime)
    format = Column(String)
    original_name = Column(String)

    user = relationship("User", back_populates="resume")
    session = relationship("Session", back_populates="resume")

class Session(Base):
    __tablename__ = "sessions"
    resume_id = Column(Integer , ForeignKey("resumes.resume_id") , nullable = False)
    user_name = Column(String  , ForeignKey("users.user_name") , nullable = False)
    job_title = Column(String  , nullable = False)
    seniority_level = Column(String , nullable = False)
    aligned_skills = Column(String)
    missing_skills = Column(String)
    alignment_percentage = Column(Float)

    __table_args__ = (
        PrimaryKeyConstraint('resume_id', 'user_name'),
    )


    user = relationship("User", back_populates="session")
    resume = relationship("Resume", back_populates="session")

