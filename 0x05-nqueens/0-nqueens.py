#!/usr/bin/python3
'''alx interview task - n queens'''
import sys


def print_solution(solution):
    """Prints the solution in the required format."""
    print(solution)


def is_safe(board, row, col, N):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    """Uses backtracking to solve the N Queens problem."""
    if row == N:
        print_solution([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col  # Place queen
            solve_nqueens(board, row + 1, N)  # Recur to place rest
            board[row] = -1  # Backtrack


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[False] * N for _ in range(N)]
    solve_nqueens(board, 0, N)


if __name__ == '__main__':
    main()
