"""
Portfolio Project 
By: Cory Simmonsen
Version 3.0
Last Updated: 9/27/2023
"""


from random import randint, shuffle
from TTT_pkg.game_model import GameBoard, Data, Player
from TTT_pkg.game_view import TicTacToe

def main():
        game = TicTacToe()
        game.play()

if __name__ == "__main__":
    main()