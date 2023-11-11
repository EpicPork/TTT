"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""

class PlayerStats(Base):
    __tablename__ = 'playerstats'

    user_id = Column(Integer, primary_key=True)
    total_wins = Column(Integer)
    total_losses = Column(Integer)

