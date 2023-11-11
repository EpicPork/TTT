"""
Portfolio Project 
By: Cory Simmonsen
Version 3.2
Last Updated: 10/27/2023
"""

import psycopg2
from psycopg2 import sql

class GameDatabase:
    def __init__(self, dbname, user, password, host, port):
        # Initialize the database connection
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    

    def insert_game_result(self, user_id, board_size, outcome):
        # Insert a game result into the 'games' table
        query = sql.SQL("INSERT INTO games (user_id, board_size, outcome) VALUES (%s, %s, %s) RETURNING game_id;")
        self.cursor.execute(query, (user_id, board_size, outcome))
        game_id = self.cursor.fetchone()[0]
        self.conn.commit()
        return game_id

    def insert_move(self, game_id, player, position_x, position_y):
        # Insert a move into the 'moves' table
        query = sql.SQL("INSERT INTO moves (game_id, player, position_x, position_y) VALUES (%s, %s, %s, %s);")
        self.cursor.execute(query, (game_id, player, position_x, position_y))
        self.conn.commit()

    def update_leaderboard(self, user_id, win=False):
        # Update the leaderboard by incrementing wins or losses
        if win:
            query = sql.SQL("UPDATE leaderboard SET wins = wins + 1 WHERE user_id = %s;")
        else:
            query = sql.SQL("UPDATE leaderboard SET losses = losses + 1 WHERE user_id = %s;")
        self.cursor.execute(query, (user_id,))
        self.conn.commit()

    def close_connection(self):
        # Close the database connection
        self.cursor.close()
        self.conn.close()

