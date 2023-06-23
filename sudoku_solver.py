import random as rand


def print_board(sudoku_board):
    """Method to print board to the terminal."""
    print("X-----------------------X")
    for i in range(len(sudoku_board)):
        if i % 3 == 0 and i != 0:
            print("|-------|-------|-------|")

        for j in range(len(sudoku_board[0])):
            if j % 3 == 0:
                print("| ", end="")

            if j == 8:
                print(sudoku_board[i][j], end=" |\n")
            else:
                print(str(sudoku_board[i][j]), end=" ")

    print("X-----------------------X\n\n")


def validate_tile(current_board, row, column, tile_value):
    """Method to Validate each tile placed on the board."""
    if tile_value in current_board[row]:
        return False

    if tile_value in [current_board[i][column] for i in range(9)]:
        return False

    start_row, start_column = row - row % 3, column - column % 3

    if tile_value in [current_board[i][j] for i in range(start_row, start_row + 3) 
                      for j in range(start_column, start_column + 3)]:
        return False

    return True


def new_sudoku_board():
    """This function generates a 9X9 grid with 17 filled tiles randomly, validating each tile with Validate Tile."""
    empty_board = [[0]*9 for _ in range(9)]
    initial_board = empty_board

    filled_tiles = 0
    while filled_tiles < 24:
        row, column, tile_value = rand.randint(0, 8), rand.randint(0, 8), rand.randint(1, 9)

        while not validate_tile(initial_board, row, column, tile_value):
            row, column, tile_value = rand.randint(0, 8), rand.randint(0, 8), rand.randint(1, 9)

        if initial_board[row][column] == 0:
            initial_board[row][column] = tile_value
            filled_tiles += 1

    print("Initial Board (24/81):")
    print_board(initial_board)

    return initial_board


def solve_sudoku_puzzle(sudoku_puzzle, row=0, column=0):
    """Method to solve the Sudoku puzzle with backtracking algorithm."""
    if column == 9:
        if row == 8:
            print("Solved Board (81/81):")
            print_board(sudoku_puzzle)
            return True

        row += 1
        column = 0

    if sudoku_puzzle[row][column] != 0:
        return solve_sudoku_puzzle(sudoku_puzzle, row, column + 1)

    for tile_value in range(1, 10):
        if validate_tile(sudoku_puzzle, row, column, tile_value):
            sudoku_puzzle[row][column] = tile_value
            if solve_sudoku_puzzle(sudoku_puzzle, row, column + 1):
                return True

    sudoku_puzzle[row][column] = 0
    return False


def main():
    print("Welcome to Kaelan's Sudoku Solver.")
    print("The program will generate a random Sudoku Puzzle with 24/81 tiles filled.")
    print("Then the program will use the backtracking algorithm to solve the puzzle.")
    print("Note: According to my testing my program will only generate solvable puzzles 43% of the time.")
    print("Rerun the program if you are getting a unsolvable puzzle. Sometimes it takes multiple runs.\n")

    if not solve_sudoku_puzzle(new_sudoku_board()):
        print("Sudoku Board is Unsolvable.\n")


if __name__ == "__main__":
    main()

