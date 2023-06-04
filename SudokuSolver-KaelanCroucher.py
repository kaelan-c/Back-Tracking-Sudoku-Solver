# CPSC 3750 - Assignment 3 - Kaelan Croucher - Sudoku Solver using Back Tracking Algorithm
import random as rand

# Method to print board to the terminal.
def printBoard(sudokuBoard):
  # Print the top line of the puzzle.
  print("X-----------------------X")
  for i in range(len(sudokuBoard)):
    # Every 3 rows print a dividing tile.
    if i % 3 == 0 and i != 0:
        print("|-------|-------|-------|")
    
    for j in range(len(sudokuBoard[0])):
      # Every 3 tiles print a verical divider.
      if j % 3 == 0:
        print( "| ", end = "")
      
      # If at the end of the row print the tile value and Vertical divider.
      if j == 8:
        print(sudokuBoard[i][j], end = " |\n")
      
      # Else just print the tile value and a spacer.
      else:
        print(str(sudokuBoard[i][j]), end = " ")
  
  # Print ending line of the puzzle
  print("X-----------------------X\n\n")

# Method to Validate each tile placed on the board.
def validateTile(currentBoard, row, column, tileValue ):

  # Check each row of the board for the tile value, if found return false.
  if tileValue in currentBoard[row]:
    return False
  
  # Check each column of the board for the tile value, if found return false.
  if tileValue in [currentBoard[i][column] for i in range(9)]:
    return False
  
  # Set the start column and row to check the 3x3 section for tile value.
  startRow, startColumn = row - row % 3, column - column % 3

  # Check each 3x3 section for the tile value, if found return false.
  if tileValue in [currentBoard[i][j] for i in range(startRow, startRow + 3) 
    for j in range(startColumn, startColumn + 3)]:
    return False
  
  return True


# This function generates a 9X9 grid with 17 filled tiles randomly, validating each tile with Validate Tile.
# It fills 24 tiles, originally I went with 17 as this is the minimum number of tiles for a unique puzzle solution.
# However 17/81 tiles felt sparse note: I have played around with this value and 24 seems to be the highest number of
# tiles that my program can relaiably create a solvable puzzle.
def newSudokuBoard():
  #This defines the base 9x9 grid where each 0 represents an empty tile.
  emptyBoard = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]
  
  # Assign empty board value to the initial board to filled.
  initialBoard = emptyBoard

  filledTiles = 0
  # Fill the initialBoard with 24 tiles validated to follow sudoku rules.
  while filledTiles < 24:
    # Generate random column number, row number and tile value using rand library.
    row, column, tileValue = rand.randint(0, 8), rand.randint(0,8), rand.randint(1,9)

    # If the previous generation was not valid, generate one until it is valid.
    while not validateTile(initialBoard, row, column, tileValue):
      row, column, tileValue = rand.randint(0, 8), rand.randint(0,8), rand.randint(1,9)

    #If valid generation assign value to tile on board.
    if initialBoard[row][column] == 0:
      initialBoard[row][column] = tileValue
      filledTiles += 1

  #Print the newly generated initial puzzle board.
  print("Inital Board:")
  printBoard(initialBoard)
  
  # Return the newly filled intital puzzle board.
  return initialBoard

def solveSudokuPuzzle(sudokuPuzzle, row = 0, column = 0):
  
  if column == 9:
    if row == 8:
      print("Solved Board:")
      printBoard(sudokuPuzzle)
      return True
    row +=1
    column = 0
  
  if sudokuPuzzle[row][column] != 0:
    return solveSudokuPuzzle(sudokuPuzzle, row, column + 1)
  
  for tileValue in range(1, 10):
    if validateTile(sudokuPuzzle, row, column, tileValue):
      sudokuPuzzle[row][column] = tileValue
      if solveSudokuPuzzle(sudokuPuzzle, row, column + 1):
        return True

  sudokuPuzzle[row][column] = 0
  return False

print("Welcome to Kaelan's Sudoku Solver.")
print("The program will generate a random Sudoku Puzzle with 24/81 tiles filled.")
print("Then the program will use the backtracking algorithm to solve the puzzle.\n")

if solveSudokuPuzzle(newSudokuBoard()) == False:
  print("Sudoku Board is Unsolvable.\n")