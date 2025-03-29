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

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_full_board():
    board = [[0] * 9 for _ in range(9)]
    for _ in range(9):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid_move(board, row, col, num) or board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num
    solve_sudoku(board)
    return board

def remove_numbers(board, count):
    puzzle_board = [row[:] for row in board]
    attempts = count
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while puzzle_board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        puzzle_board[row][col] = 0
        attempts -= 1
    return puzzle_board

def generate_sudoku():
    full_board = generate_full_board()
    puzzle_board = remove_numbers(full_board, 40)
    print("Generated Sudoku Puzzle:")
    print_board(puzzle_board)
    return puzzle_board

if __name__ == "__main__":
    generate_sudoku()