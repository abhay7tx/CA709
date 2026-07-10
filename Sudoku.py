def rotate(row, k):
    return row[k:] + row[:k]

row1 = [1,2,3,4,5,6,7,8,9]

board = []
board.append(row1)

for i in range(1, 9):
    if i % 3 == 0:
        board.append(rotate(board[i-3], 1))
    else:
        board.append(rotate(board[i-1], 3))

for row in board:
    print(*row)