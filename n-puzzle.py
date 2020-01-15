import sys
import helpers
import solver
import puzzleParser
import argparse
import heuristic

usedHeuristic = heuristic.manhattanDistance

def main():
    puzzleSize = puzzleParser.getPuzzleSize()
    puzzle = puzzleParser.getPuzzle(puzzleSize)

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
    parser = argparse.ArgumentParser(description='N-puzzle solver using A* algorithm')

    # Heuristic functions args
    parser.add_argument('-M', '--manhattan', action='store_true', help='an integer for the accumulator')

    args = parser.parse_args()

    if (args.manhattan):
        print("manhattan")
        usedHeuristic = heuristic.manhattanDistance

    main()