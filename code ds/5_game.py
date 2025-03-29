import random

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    box_x, box_y = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_x + i][box_y + j] == num:
                return False
    return True

def get_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_cell = get_empty_cell(board)
    if empty_cell is None:
        return True
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def remove_numbers(board, count):
    attempts = count
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
        attempts -= 1

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)
    return board

def play_sudoku():
    base_board = generate_sudoku()
    puzzle_board = [row[:] for row in base_board]
    remove_numbers(puzzle_board, 40)
    
    chances = 20
    while chances > 0:
        print_board(puzzle_board)
        row, col, num = map(int, input("Enter row, column, and number (1-9) (e.g., 1 2 5): ").split())
        row, col = row - 1, col - 1
        
        if puzzle_board[row][col] == 0 and is_valid_move(puzzle_board, row, col, num):
            puzzle_board[row][col] = num
            if puzzle_board == base_board:
                print("Congratulations! You completed the Sudoku.")
                return
        else:
            chances -= 1
            print(f"Incorrect move! {chances} chances remaining.")
            print(f"The correct number for ({row + 1}, {col + 1}) is {base_board[row][col]}")
    
    print("Game Over! You have used all your chances.")
    print("The correct board was:")
    print_board(base_board)

play_sudoku()
