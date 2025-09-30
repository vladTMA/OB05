# board.py
import pygame

from typing import List, Optional
from piece import Piece
from config import BOARD_SIZE

def initialize_board() -> List[List[Optional[Piece]]]:
    board: List[List[Optional[Piece]]] = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    back_row = ['♜', '♞', '♝♞', '♝', '♛', '♚', '♝', '♜♞', '♞', '♜']

    for col in range(BOARD_SIZE):
        board[0][col] = Piece(back_row[col], 'black')
        board[1][col] = Piece('♟', 'black')
        board[8][col] = Piece('♙', 'white')
        board[9][col] = Piece(
            back_row[col].replace('♜', '♖')
                         .replace('♞', '♘')
                         .replace('♝', '♗')
                         .replace('♛', '♕')
                         .replace('♚', '♔'),
            'white'
        )

    return board
