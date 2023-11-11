"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""


from game.game_database import GameDatabase
from game.game_model import GameBoard, Data, Player
from game.game_view import TicTacToe
# Your other imports and code here...

def main():
    # Initialize the database connection
    db = GameDatabase(
        dbname='your_dbname',
        user='your_dbuser',
        password='your_dbpassword',
        host='your_dbhost',
        port='your_dbport'
    )

    game = TicTacToe()
    game.play(db)  # Pass the GameDatabase instance to your game

    # Close the database connection when done
    db.close_connection()

if __name__ == "__main__":
    main()
