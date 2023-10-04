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
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(n) for _ in range(n)]]
    solutions = []

    def solve(col):
        if col == n:
            solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(col + 1)
                board[row][col] = 0
        solve(0)
        for solution in solutions:
            print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(N)