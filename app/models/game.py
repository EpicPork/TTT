"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""



class Games(Base):
    __tablename__ = 'games'

    game_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    board_size = Column(Integer, nullable=False)
    outcome = Column(String(10))

    # Define foreign key relationship with User table if needed
    user = relationship("User", back_populates="games")
