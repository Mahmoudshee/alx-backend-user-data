#!/usr/bin/env python3
"""
User model definition.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    User class representing the 'users' table in the database.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email, hashed_password, session_id=None, reset_token=None):
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

# Run the script to check the output
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Replace 'DATABASE_URI' with the actual database URI
    DATABASE_URI = 'sqlite:///example.db'
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))
