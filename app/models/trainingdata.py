"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""


from sqlalchemy import String

class TrainingData(Base):
    __tablename__ = 'trainingdata'

    game_id = Column(String)
    player = Column(String(10))
    position_x = Column(Integer)
    position_y = Column(Integer)