def issafe(i,j,board,c):
    for k in range(len(board[i])):
        if board[i][k]==c:
            return False
    for k in range(len(board)):
        if board[k][j]==c:
            return False
    x=(i//3)*3
    y=(j//3)*3
    for row in range(x,x+3):
        for col in range(y,y+3):
            if board[row][col]==c:
                return False
    return True

def solve(i,j,board):
    if j>=len(board[0]):
        j=0
        i+=1
    if i>=len(board):
        return True
    if board[i][j]!='.':
        return solve(i,j+1,board)
    if board[i][j]=='.':
        for k in range(1,10):
            c=str(k)
            if issafe(i,j,board,c):
                board[i][j]=c
                if solve(i,j+1,board):
                    return True
                board[i][j]='.'
    return False

board=[
['5','3','.','.','7','.','.','.','.'],
['6','.','.','1','9','5','.','.','.'],
['.','9','8','.','.','.','.','6','.'],
['8','.','.','.','6','.','.','.','3'],
['4','.','.','8','.','3','.','.','1'],
['7','.','.','.','2','.','.','.','6'],
['.','6','.','.','.','.','2','8','.'],
['.','.','.','4','1','9','.','.','5'],
['.','.','.','.','8','.','.','7','9']
]

print("Before")
for row in board:
    print(*row)

solve(0,0,board)

print("After")
for row in board:
    print(*row)