"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""

class Moves(Base):
    __tablename__ = 'moves'

    move_id = Column(Integer, primary_key=True)
    game_id = Column(Integer)
    player = Column(String(10))
    position_x = Column(Integer)
    position_y = Column(Integer)
