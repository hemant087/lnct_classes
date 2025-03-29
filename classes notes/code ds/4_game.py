import random

# Sudoku Solver using Backtracking
def is_valid(board, row, col, num):
    """ Check if num can be placed at board[row][col] """
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    """ Solves the Sudoku using Backtracking """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False  # No valid number found
    return True

def print_sudoku(board):
    """ Print Sudoku in a readable format """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

# Generate a random Sudoku puzzle (with empty spaces)
def generate_sudoku():
    """ Generate a Sudoku puzzle with random empty spaces """
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)  # Start with a solved board

    # Remove numbers randomly to create a puzzle
    for _ in range(random.randint(40, 50)):  # Remove 40-50 numbers for difficulty
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

# Manual Sudoku Play
def play_sudoku():
    """ User plays Sudoku manually with 10 chances """
    board = generate_sudoku()
    original_board = [row[:] for row in board]  # Copy to keep track of original puzzle
    chances = 10  # Total chances
    
    while chances > 0:
        print("\nCurrent Sudoku Board:")
        print_sudoku(board)

        # Get user input
        row, col, num = map(int, input("\nEnter row, column, and number (1-9) [e.g., 3 2 5]: ").split())
        row -= 1  # Convert to 0-indexed
        col -= 1  

        # Check if the position is a fixed number
        if original_board[row][col] != 0:
            print("❌ Cannot change a pre-filled number! Try again.")
            continue

        # Validate user input
        if is_valid(board, row, col, num):
            board[row][col] = num
            print("✅ Correct move!")
        else:
            chances -= 1
            print(f"❌ Wrong move! Chances left: {chances}")

        # Check if the board is fully solved
        if all(0 not in row for row in board):
            print("\n🎉 Congratulations! You solved the Sudoku! 🎉")
            print_sudoku(board)
            return

    print("\n😞 Game Over! You ran out of chances. Here's the correct solution:")
    solve_sudoku(board)  # Solve the board
    print_sudoku(board)

# Main Menu
def main():
    while True:
        print("\n🎮 Welcome to Sudoku Game 🎮")
        print("1️⃣ Solve a Sudoku puzzle")
        print("2️⃣ Play Sudoku manually (10 chances)")
        print("3️⃣ Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            board = generate_sudoku()
            print("\n🔍 Unsolved Sudoku:")
            print_sudoku(board)
            print("\n🧠 Solving...")
            solve_sudoku(board)
            print("\n✅ Solved Sudoku:")
            print_sudoku(board)

        elif choice == "2":
            play_sudoku()
        elif choice == "3":
            print("👋 Goodbye! Thanks for playing Sudoku.")
            break
        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
