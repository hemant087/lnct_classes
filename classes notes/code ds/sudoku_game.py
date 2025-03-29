def is_valid(board,row, col, num):
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


def sudoku_solver(board):
    for row in range(9): 
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board, row,col,num):
                        board[row][col]=num
                        # sudoku_solver(board)
                        if sudoku_solver(board):
                            return True
                        else:
                            board[row][col] = 0
                return False   
    return True






board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


if sudoku_solver(board):
    for i in board:
        print(i)
else:
    print("not valid board")
