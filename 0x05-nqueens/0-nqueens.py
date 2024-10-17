#!/usr/bin/python3
import sys

# Function to check if a queen can be placed on board[row][col]
def is_safe(board, row, col, N):
    # Check the column for any queen
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

# Recursive function to solve N Queens
def solve_nqueens(N, row, board, solutions):
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

# Main function to handle input and start solving
def nqueens():
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
    
    solutions = []
    board = [-1] * N  # Array to store the position of queens
    solve_nqueens(N, 0, board, solutions)
    
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    nqueens()
