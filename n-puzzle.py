import sys
import helpers
import solver
import parser

def main():
    puzzleSize = parser.getPuzzleSize()
    print("Puzzle size: " + str(puzzleSize))
    print("Initial state:")

    puzzle = [[]] * puzzleSize

    for i, line in enumerate(sys.stdin):
        puzzle[i] = list(map(int, parser.filterCommentFromLine(line).split()))

    helpers.debugPuzzle(puzzle)

    if solver.isSolvable(puzzle) == False:
        helpers.exit("Puzzle is not solvable")

    finalState = solver.getFinalPuzzle(puzzleSize)

    print("Goal state:")

    helpers.debugPuzzle(finalState)

    solver.startSolving(puzzle, finalState)

if __name__ == "__main__":
    main()