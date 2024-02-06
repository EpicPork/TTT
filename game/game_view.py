"""
Tic Tac Toe Game
By: Cory Simmonsen
Version 3.4
Last Updated: 12/20/2023
"""

from random import shuffle
from typing import Any
from pygame  import Any
from .game_model import Data, Player, TicTacToe
from .game_database import 

class TicTacToe:
    def __init__(self, database):
        """
        Initialize the TicTacToe game.
        
        Args:
            database: The database instance to use for storing game results and leaderboard.
        """
        self.data = Data()
        self.player = None
        self.player_turn = True  # Initialize player turn
        self.database = database  # Pass the database instance
        self.game_board = None
        self.screen = None
        self.clock = None

    def init_pygame(self):
        """
        Initialize Pygame and set up the game window.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((900, 900))  # Set screen size to 900x900
        pygame.display.set_caption("Tic Tac Toe")
        self.clock = pygame.time.Clock()  # For controlling frame rate

    def draw_board(self):
        """
        Draw the game board and pieces on the screen.
        """
        # Code to draw the game board based on self.game_board.board
        # and the current size of the board
        # Example: Draw grid lines, Xs, and Os
        pass

    def handle_events(self):
        """
        Handle Pygame events, like mouse clicks.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Exit the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse click events
                # Convert mouse position to board coordinates and make a move
                pass

    def play_pygame(self):
        """
        Start and play a game of Tic Tac Toe using Pygame.
        """
        self.init_pygame()
        running = True
        while running:
            self.handle_events()
            self.screen.fill((255, 255, 255))  # Fill screen with white
            self.draw_board()
            pygame.display.update()  # Update the display
            self.clock.tick(60)  # Limit frame rate to 60 FPS

        pygame.quit()

    # ... existing methods from your original game_view.py ...

# Remember, you may need to adjust the Player and Data classes for GUI-based interaction.

# Additional code for handling board drawing, input conversion, and database integration
# should be implemented based on your specific game logic and requirements.

    def select_board_size(self):
        """
        Prompt the user to select the board size and return the chosen size.

        Returns:
            int: The selected board size.
        """
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
        """
        Start and play a game of Tic Tac Toe.
        """
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
        """
        Display the leaderboard to the user.
        """
        leaderboard = self.database.fetch_leaderboard()  # Fetch the leaderboard from the database
        for entry in leaderboard:
            username, wins, losses, draws = entry
            print(f"{username} - Wins: {wins}, Losses: {losses}, Draws: {draws}")

    def reset_game(self):
        """
        Reset the game for a new round.
        """
        self.data = Data()
        self.player = None
        self.player_turn = True

