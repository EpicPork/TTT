"""
Portfolio Project 
By: Cory Simmonsen
Version 3.3
Last Updated: 11/02/2023
"""

from random import shuffle
from .game_model import Data, Player, GameBoard
from .game_database import GameDatabase

class TicTacToe:
    def __init__(self, database):
        self.data = Data()
        self.player = None
        self.player_turn = True  # Initialize player turn
        self.database = database  # Pass the database instance

    def select_board_size(self):
        while True:
            try:
                size = int(input("Choose the board size (3, 4, 5, or 6): "))
                if size in [3, 4, 5, 6]:
                    return size
                else:
                    print("Invalid input. Choose from 3, 4, 5, or 6.")
            except ValueError:
                print("Invalid input. Choose from 3, 4, 5, or 6.")

    def play(self):
        self.data.prompt_player_name()
        print(f"Welcome, {self.data.player_name}!\n")
        print("Let's play Tic Tac Toe!\n")

        self.data.prompt_player_symbol()
        print(f"You've chosen to play as {self.data.player_symbol}.\n")
        self.data.computer_symbol = "O" if self.data.player_symbol == "X" else "X"

        self.data.display_instructions()

        self.data.prompt_computer_first()
        if self.data.computer_first.lower() == 'y':
            self.player_turn = False
        else:
            self.player_turn = True

        self.data.set_difficulty_level()
        print(f"The computer is playing at difficulty level {self.data.difficulty_level}.\n")

        # Prompt the user to select the board size
        board_size = self.select_board_size()
        self.game_board = GameBoard(board_size)  # Pass the selected size to GameBoard

        while True:
            self.game_board.print_board()

            if self.player_turn:
                print("It's your turn.\n")
                self.player = Player(self.data.player_name, self.data.player_symbol)
                self.player.make_move(self.game_board)
                winner = self.game_board.check_winner()  # Check for a winner after each player's move
                if winner:
                    self.game_board.print_board()
                    self.data.display_result(winner)
                    # Insert game result into the database
                    user_name = self.data.player_name  # Get the user's name
                    game_result = winner
                    self.database.insert_game_result(user_name, self.game_board.size, game_result)
                    # Update the leaderboard
                    self.database.update_leaderboard(user_name, game_result)
                    break
                self.player_turn = False
            else:
                print("It's the computer's turn.\n")
                self.data.computer_move(self.game_board, self.data.difficulty_level, self.data.player_symbol)
                winner = self.game_board.check_winner()  # Check for a winner after each computer's move
                if winner:
                    self.game_board.print_board()
                    self.data.display_result(winner)
                    # Insert game result into the database
                    user_name = "Computer"  # Set the user name as "Computer"
                    game_result = winner
                    self.database.insert_game_result(user_name, self.game_board.size, game_result)
                    # Update the leaderboard
                    self.database.update_leaderboard(user_name, game_result)
                    break
                self.player_turn = True

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            self.reset_game()
            self.play()
        else:
            print("Bye! Thanks for Playing!")

    def display_leaderboard(self):
        """Display the leaderboard to the user."""
        leaderboard = self.database.fetch_leaderboard()  # Fetch the leaderboard from the database
        for entry in leaderboard:
            username, wins, losses, draws = entry
            print(f"{username} - Wins: {wins}, Losses: {losses}, Draws: {draws}")

    def reset_game(self):
        self.data = Data()
        self.player = None
        self.player_turn = True
