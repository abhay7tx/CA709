def safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def queen(board, row, n):

    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()
        print()
        return

    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = 1
            queen(board, row + 1, n)
            board[row][col] = 0      # Backtrack


n = int(input("Enter n: "))

board = [[0] * n for i in range(n)]

queen(board, 0, n)