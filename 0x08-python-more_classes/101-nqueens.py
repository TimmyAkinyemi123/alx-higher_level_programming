#!/usr/bin/python3
# 101-nqueens.py

import sys

def is_safe(board, row, col):
    """Checks if a queen can be placed at board[row][col]
    without conflicts.
    Args:
        row: row of the chessboard
        col: column of the chessboard
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip (range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(n):
    if
