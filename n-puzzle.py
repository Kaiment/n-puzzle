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

    if solver.isSolvable(puzzle) == False:
        helpers.exit("Puzzle is not solvable")

    finalState = solver.getFinalPuzzle(puzzleSize)

    print("Goal state:")

    helpers.debugPuzzle(finalState)

    solver.aStar(puzzle, finalState)

if __name__ == "__main__":
    main()