"""
Python 3.9.6 (default, Aug 11 2023, 19:44:49) 
[Clang 15.0.0 (clang-1500.0.40.1)] on darwin
Version 3.2
Tic Tac Toe 
"""

from sqlalchemy.orm import relationship
from sqlalchemy.orm import Relationship
from sqlalchemy.orm import Bundle
from typing_extensions import Annotated
from sqlalchemy.orm import reconstructor
from psycopg2 import 

from random import shuffle
from game import game_model
from game import game_view
from game import game_database