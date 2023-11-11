"""
Portfolio Project 
By: Cory Simmonsen
Version 3.3
Last Updated: 11/02/2023
"""

from psycopg2 import sql

class GameDatabase:
    def __init__(self, dbname, user, password, host, port):
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

    def insert_game_result(self, user_id, board_size, outcome):
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
        # Fetch the leaderboard data from the 'leaderboard' table
        query = "SELECT username, wins, losses, draws FROM leaderboard ORDER BY wins DESC, losses ASC;"
        self.cursor.execute(query)
        leaderboard = self.cursor.fetchall()
        return leaderboard

    def update_leaderboard(self, user_id, win=False):
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
        try:
            # Close the database connection
            self.cursor.close()
            self.conn.close()
        except psycopg2.Error as e:
            # Handle potential errors when closing the connection.
            raise e

