"""
Portfolio Project 
By: Cory Simmonsen
Version 3.3
Last Updated: 11/02/2023
"""

import psycopg2 

class GameDatabase:
    def __init__(self, dbname, user, password, host, port):
        """
        Initialize the GameDatabase with a database connection.

        Args:
            dbname (str): The name of the database.
            user (str): The database user.
            password (str): The user's password.
            host (str): The database host.
            port (int): The database port.
        """
        try:
            # Initialize the database connection
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.conn.cursor()
        except psycopg2.OperationalError as e:
            # Handle database connection error, e.g., connection credentials or server availability.
            raise e

    # ... (rest of your code)


    def insert_game_result(self, user_id, board_size, outcome):
        """
        Insert a game result into the 'games' table.

        Args:
            user_id (int): The user's ID.
            board_size (int): The size of the game board.
            outcome (str): The outcome of the game.

        Returns:
            int: The ID of the inserted game result.
        """
        try:
            # Insert a game result into the 'games' table
            query = sql.SQL("INSERT INTO games (user_id, board_size, outcome) VALUES (%s, %s, %s) RETURNING game_id;")
            self.cursor.execute(query, (user_id, board_size, outcome))
            game_id = self.cursor.fetchone()[0]
            self.conn.commit()
            return game_id
        except psycopg2.Error as e:
            # Handle database insert error, e.g., unique constraint violation.
            self.conn.rollback()  # Rollback the transaction in case of an error.
            raise e

    def insert_move(self, game_id, player, position_x, position_y):
        """
        Insert a move into the 'moves' table.

        Args:
            game_id (int): The ID of the game.
            player (str): The player's symbol.
            position_x (int): The X-coordinate of the move.
            position_y (int): The Y-coordinate of the move.
        """
        try:
            # Insert a move into the 'moves' table
            query = sql.SQL("INSERT INTO moves (game_id, player, position_x, position_y) VALUES (%s, %s, %s, %s);")
            self.cursor.execute(query, (game_id, player, position_x, position_y))
            self.conn.commit()
        except psycopg2.Error as e:
            # Handle database insert error, e.g., foreign key constraint violation.
            self.conn.rollback()  # Rollback the transaction in case of an error.
            raise e

    def fetch_leaderboard(self):
        """
        Fetch the leaderboard data from the 'leaderboard' table.

        Returns:
            list: A list of leaderboard entries containing username, wins, losses, and draws.
        """
        query = "SELECT username, wins, losses, draws FROM leaderboard ORDER BY wins DESC, losses ASC;"
        self.cursor.execute(query)
        leaderboard = self.cursor.fetchall()
        return leaderboard

    def update_leaderboard(self, user_id, win=False):
        """
        Update the leaderboard by incrementing wins or losses for a user.

        Args:
            user_id (int): The user's ID.
            win (bool): True if the user won the game, False if the user lost.
        """
        try:
            # Update the leaderboard by incrementing wins or losses
            if win:
                query = sql.SQL("UPDATE leaderboard SET wins = wins + 1 WHERE user_id = %s;")
            else:
                query = sql.SQL("UPDATE leaderboard SET losses = losses + 1 WHERE user_id = %s;")
            self.cursor.execute(query, (user_id,))
            self.conn.commit()
        except psycopg2.Error as e:
            # Handle database update error, e.g., user not found in the leaderboard.
            self.conn.rollback()  # Rollback the transaction in case of an error.
            raise e

    def close_connection(self):
        """
        Close the database connection.
        """
        try:
            # Close the database connection
            self.cursor.close()
            self.conn.close()
        except psycopg2.Error as e:
            # Handle potential errors when closing the connection.
            raise e
{}