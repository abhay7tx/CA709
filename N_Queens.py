# Check if we can place a queen at (row, col)
def isSafe(board, row, col, n):

    # Check the same column above
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    # No queen is attacking this position
    return True


# Try to place queens row by row
def solve(board, row, n):

    # If all rows are filled, solution is found
    if row == n:
        return True

    # Try every column in the current row
    for col in range(n):

        # Can we place a queen here?
        if isSafe(board, row, col, n):

            # Place the queen
            board[row][col] = 'Q'

            # Try placing queen in the next row
            if solve(board, row + 1, n):
                return True

            # Didn't work, remove the queen (Backtracking)
            board[row][col] = '.'

    # No column worked in this row
    return False


# Size of chessboard
n = 8

# Create an empty board
board = [['.' for _ in range(n)] for _ in range(n)]

# Find one valid solution
solve(board, 0, n)

# Print the board
for row in board:
    print(" ".join(row))