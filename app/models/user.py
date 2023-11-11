"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""

from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(255))

    # Define a one-to-one relationship with the Leaderboard table
    leaderboard = relationship("Leaderboard", uselist=False, back_populates="user")

    # Define other attributes and methods in your User class...

