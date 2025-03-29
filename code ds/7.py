import random



def is_valid_move(board,row, col, num):
    for i in range(9):
        # checking row
        if board[row][i] == num:
            return False
        # checking column
        if board[i][col] == num:
            return False
        
        # check the matrix of 3x3

        start_row = 3*(row//3)
        start_col = 3*(col//3)
        for i in range(3): # i = 0,1,2
            for j in range(3): #j = 0,1,2
                if board[start_row+i][start_col+j] == num:
                    return False
    return True

board = [[0] * 9 for _ in range(9)]
for _ in range(9):
    row, col = random.randint(0, 8), random.randint(0, 8)
    num = random.randint(1, 9)
    while not is_valid_move(board, row, col, num) or board[row][col] != 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
    board[row][col] = num

for i in board:
    print(i)

    
