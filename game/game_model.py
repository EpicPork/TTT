"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""

# app/game/game_model.py

from random import shuffle
from app.game.game_database import GameDatabase  # Update the import path
from app.models import User  # Update the import path if needed

class GameBoard:
    def __init__(self, size):
        # Initialize the game board with the specified size
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.database = GameDatabase()  # Create an instance of GameDatabase

    def print_board(self):
        # Print the current state of the game board
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    print(" ", end="")
                else:
                    print(self.board[i][j], end="")
                if j != self.size - 1:
                    print(" | ", end="")
            print()
            if i != self.size - 1:
                print("-" * (4 * self.size - 1))

    def get_user_id(self, username):
        # This method retrieves the user's ID based on the username
        user = db.session.query(User).filter(User.username == username).first()
        if user:
            return user.user_id
        else:
            return None  # Handle the case where the user is not found

    def make_move(self, row, col, symbol):
        # Make a move on the game board at the specified row and column with the given symbol
        if self.board[row][col] != " ":
            return False
        self.board[row][col] = symbol
        return True

    def check_winner(self):
        # Check for a winning condition (rows, columns, diagonals)
        for row in range(self.size):
            if self.board[row][0] != " " and all(self.board[row][col] == self.board[row][0] for col in range(1, self.size)):
                return self.board[row][0]

        for col in range(self.size):
            if self.board[0][col] != " " and all(self.board[row][col] == self.board[0][col] for row in range(1, self.size)):
                return self.board[0][col]

        if self.board[0][0] != " " and all(self.board[i][i] == self.board[0][0] for i in range(1, self.size)):
            return self.board[0][0]

        if self.board[0][self.size - 1] != " " and all(self.board[i][self.size - 1 - i] == self.board[0][self.size - 1] for i in range(1, self.size)):
            return self.board[0][self.size - 1]

        if all(self.board[i][j] != " " for i in range(self.size) for j in range(self.size)):
            return "Draw"

        return None

    def game_over(self):
        # Check if the game is over (e.g., no more empty spaces)
        return all(self.board[i][j] != " " for i in range(self.size) for j in range(self.size))

    def end_game(self, result):
        # Save the game result in the database
        user_id = self.get_user_id(self.player_name)  # Call the get_user_id method
        if user_id:
            self.database.insert_game_result(user_id, self.size, result)  # Update to include size
            self.database.update_leaderboard(user_id, result)  # Update the leaderboard
        else:
            print("User not found. Cannot save game result.")


class Player:
    def __init__(self, name, symbol):
        # Initialize a player with a name and symbol (X or O)
        self.name = name
        self.symbol = symbol

    def make_move(self, game_board):
        # Prompt the player to make a move on the game board
        while True:
            try:
                move = int (input("Select a position (1-{}):, ").format(game_board.size ** 2))
                if 1 <= move <= game_board.size ** 2:
                    move -= 1
                    row = move // game_board.size
                    col = move % game_board.size
                    if game_board.make_move(row, col, self.symbol): 
                        break
                    else:
                        print("Invalid move. Position already taken.")
                else:
                    print("Invalid input. Enter a number between 1 and {}.".format(game_board.size ** 2))
            except ValueError:
                print("Invalid input. Enter a number between 1 and {}.".format(game_board.size ** 2))
                

class Data:
    def __init__(self):
        # Initialize data attributes
        self.player_name = ""
        self.player_symbol = ""
        self.computer_symbol = ""
        self.computer_first = False
        self.difficulty_level = 0
        self.board_size = 0  # Add board size attribute

    def set_difficulty_level(self):
        # Prompt the user to set the difficulty level
        while True:
            try:
                self.difficulty_level = int(input("Choose the difficulty level (1 for easy, 2 for medium, 3 for hard): "))
                if self.difficulty_level in [1, 2, 3]:
                    break
                else:
                    print("Invalid input. Choose from 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Choose from 1, 2, or 3.")

    def evaluate(self, game_board, player_symbol):
        # Evaluate the current game state
        winner = game_board.check_winner()

        if winner == self.computer_symbol:
            return 1
        elif winner == player_symbol:
            return -1
        elif winner == "Draw":
            return 0
        else:
            return 0.5

    def prompt_player_name(self):
        # Prompt the player to enter their name
        self.player_name = input("Enter your name: ").strip()

    def prompt_player_symbol(self):
        # Prompt the user to choose their symbol (X or O)
        while True:
            symbol = input("Choose your symbol (X or O): ").strip().upper()
            if symbol == 'X' or symbol == 'O':
                self.player_symbol = symbol
                break
            else:
                print("Invalid input. Choose either X or O.")

    def display_instructions(self):
        # Display game instructions
        print("Instructions:")
        print("1. The game board consists of a grid.")
        print("2. Each player takes turns to place their symbol (X or O) on the board.")
        print("3. The player who succeeds in placing three of their symbols in a row, column, or diagonal wins the game.")
        print("4. The game ends in a draw if the board is filled with symbols and no player wins.")
        print()

    def prompt_computer_first(self):
    # Prompt the user to choose if the computer should go first
        while True:
            choice = input("Do you want the computer to go first? (y/n): ")
            if choice.lower() == 'y' or choice.lower() == 'n':
                self.computer_first = choice.lower()  # Update the data attribute
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

    def prompt_board_selection(self):
        # Prompt for board size (3, 4, 5, or 6)
        while True:
            try:
                self.board_size = int(input("Choose the board size (3, 4, 5, or 6): "))
                if self.board_size in [3, 4, 5, 6]:
                    return self.board_size
                else:
                    print("Invalid input. Choose from 3, 4, 5, or 6.")
            except ValueError:
                print("Invalid input. Choose from 3, 4, 5, or 6.")

    def minimax(self, game_board, depth, maximizing_player, player_symbol, alpha=float('-inf'), beta=float('inf')):
        # Implement the minimax algorithm for the computer player
        if depth == 0 or game_board.game_over():
            return self.evaluate(game_board, player_symbol)

        if maximizing_player:
            max_score = float('-inf')
            for move in self.available_moves(game_board):
                row, col = move
                game_board.make_move(row, col, self.computer_symbol)
                score = self.minimax(game_board, depth - 1, False, player_symbol, alpha, beta)
                game_board.board[row][col] = " "
                max_score = max(max_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return max_score
        else:
            min_score = float('inf')
            for move in self.available_moves(game_board):
                row, col = move
                game_board.make_move(row, col, player_symbol)
                score = self.minimax(game_board, depth - 1, True, player_symbol, alpha, beta)
                game_board.board[row][col] = " "
                min_score = min(min_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score

    def computer_move(self, game_board, depth, player_symbol):
        # Make a move for the computer player using the minimax algorithm
        best_score = float('-inf')
        best_move = None
        opponent_symbol = 'X' if self.computer_symbol == 'O' else 'O'

        available_moves = self.available_moves(game_board)
        shuffle(available_moves)  # Shuffle available moves

        for move in available_moves:
            row, col = move
            game_board.make_move(row, col, self.computer_symbol)

            if game_board.check_winner() == self.computer_symbol:
                score = 1
            elif game_board.check_winner() == opponent_symbol:
                score = -1
            elif depth == 0 or game_board.check_winner() == "Draw":
                score = 0
            else:
                score = self.minimax(game_board, depth - 1, False, player_symbol)

            game_board.board[row][col] = " "

            if score > best_score:
                best_score = score
                best_move = move

        row, col = best_move
        game_board.make_move(row, col, self.computer_symbol)

        
    def available_moves(self, game_board):
        # Get a list of available moves on the game board
        moves = []
        for row in range(game_board.size):
            for col in range(game_board.size):
                if game_board.board[row][col] == " ":
                    moves.append((row, col))
        return moves
    
    def display_result(self, winner):
        # Display the result of the game
        if winner == self.player_symbol:
            print("Congratulations! You won!")
        elif winner == self.computer_symbol:
            print("Sorry, you lost!")
            # Check for a draw condition
        else: winner is None
        print("It's a draw!")

    def end_game(self, result):
        # Save the game result in the database
        user_id = self.get_user_id(self.player_name)
        if user_id:
            insert_game_result(user_id, result, self.moves)
            update_leaderboard(user_id, result)
        else:
            print("User not found. Cannot save game result.")

    # You'll need to implement the get_user_id method
