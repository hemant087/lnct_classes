def is_valid(board,row,col,num):
    # for row checking
    for i in range(9):
        if board[i][col] == num:
            return False
        
        if board[row][i] == num:
            return False
        
    # for checking 3x3 box

    start_row,start_col = 3*(row//3),3*(col//3)

    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False
    return True



def sudoku_solver(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board,row,col,num):
                        board[row][col]= num
                        if sudoku_solver(board):
                            return True
                        else:
                            board[row][col]=0
                return False
    return True

sudoku_board = [
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


if sudoku_solver(sudoku_board):
    for i in sudoku_board:
        print(i)
else:
    print("No solution exists.")

