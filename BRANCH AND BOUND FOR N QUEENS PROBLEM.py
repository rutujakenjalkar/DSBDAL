boardsize = 4  # Size of the chess board (5x5)

# Arrays to keep track of constraints for branch and bound
cols = [False] * boardsize
left_diagonals = [False] * (2 * boardsize - 1)  # row - col + (N-1)
right_diagonals = [False] * (2 * boardsize - 1)  # row + col

# Initialize board
board = [[0 for _ in range(boardsize)] for _ in range(boardsize)]

# Function to print the board
def printSolution():
    for i in range(boardsize):
        for j in range(boardsize):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print("-" * (2 * boardsize))

# Recursive function using backtracking and branch & bound
def solveNQueens(col):
    if col >= boardsize:
        printSolution()
        return True  # Change to False if you want all solutions

    res = False
    for row in range(boardsize):
        if (not cols[row] and
            not left_diagonals[row - col + boardsize - 1] and
            not right_diagonals[row + col]):

            # Place queen
            board[row][col] = 1
            cols[row] = True
            left_diagonals[row - col + boardsize - 1] = True
            right_diagonals[row + col] = True

            # Recur to place rest of the queens
            res = solveNQueens(col + 1) or res

            # Backtrack
            board[row][col] = 0
            cols[row] = False
            left_diagonals[row - col + boardsize - 1] = False
            right_diagonals[row + col] = False

    return res

# Call the function starting from the first column
solveNQueens(0)
