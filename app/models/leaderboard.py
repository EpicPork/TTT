"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Leaderboard(Base):
    __tablename__ = 'leaderboard'

    user_id = Column(Integer, primary_key=True)
    wins = Column(Integer)
    losses = Column(Integer)
    draws = Column(Integer)  # Add a new column for draws

    # Define a one-to-one relationship with the User table
    user = relationship("User", uselist=False, back_populates="leaderboard")
