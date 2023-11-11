"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""

class TrainingData(Base):
    __tablename__ = 'trainingdata'

    game_id = Column(Integer)
    player = Column(String(10))
    position_x = Column(Integer)
    position_y = Column(Integer)
