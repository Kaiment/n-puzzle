import sys
import helpers
import solver
import parser

def main():
    puzzleSize = parser.getPuzzleSize()
    print("Puzzle size: " + str(puzzleSize))
    print("Initial state:")

    puzzle = parser.getPuzzle(puzzleSize)

    helpers.debugPuzzle(puzzle)

    goal = solver.getFinalPuzzle(puzzleSize)
    print("Goal state:")
    helpers.debugPuzzle(goal)

    if solver.isSolvable(puzzle, goal) == False:
        helpers.exit("Puzzle is not solvable")

    solver.idaStar(puzzle, goal)

if __name__ == "__main__":
    main()