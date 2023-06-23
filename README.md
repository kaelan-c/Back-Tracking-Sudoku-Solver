# BackTrackingSudokuSolver
Small Sudoku solving program written in Python using the Back Tracking Algorithm.

Sample Output:

```text
Welcome to Kaelan's Sudoku Solver.
The program will generate a random Sudoku Puzzle with 24/81 tiles filled.
Then the program will use the backtracking algorithm to solve the puzzle.
Note: According to my testing my program will only generate solvable puzzles 43% of the time.
Rerun the program if you are getting a unsolvable puzzle. Sometimes it takes multiple runs.

Initial Board (24/81):
X-----------------------X
| 0 0 0 | 0 2 5 | 3 0 9 |
| 9 0 0 | 0 0 0 | 0 0 8 |
| 5 0 0 | 0 0 7 | 0 0 0 |
|-------|-------|-------|
| 0 9 0 | 0 0 0 | 5 3 0 |
| 0 2 0 | 0 0 0 | 0 8 0 |
| 0 1 0 | 0 7 0 | 6 4 0 |
|-------|-------|-------|
| 0 0 8 | 0 0 0 | 1 2 0 |
| 0 0 0 | 0 0 0 | 0 9 0 |
| 6 5 0 | 2 0 0 | 0 0 0 |
X-----------------------X


Solved Board (81/81):
X-----------------------X
| 1 4 7 | 8 2 5 | 3 6 9 |
| 9 6 2 | 1 3 4 | 7 5 8 |
| 5 8 3 | 6 9 7 | 2 1 4 |
|-------|-------|-------|
| 7 9 6 | 4 8 2 | 5 3 1 |
| 3 2 4 | 5 1 6 | 9 8 7 |
| 8 1 5 | 3 7 9 | 6 4 2 |
|-------|-------|-------|
| 4 7 8 | 9 5 3 | 1 2 6 |
| 2 3 1 | 7 6 8 | 4 9 5 |
| 6 5 9 | 2 4 1 | 8 7 3 |
X-----------------------X
```
