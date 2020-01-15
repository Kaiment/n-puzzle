import sys
import helpers
import solver
import parser
import argparse
import heuristic

def main(args):
    puzzleSize = parser.getPuzzleSize()
    puzzle = parser.getPuzzle(puzzleSize)

    print("Puzzle size: " + str(puzzleSize))
    print("Initial state:")

    helpers.debugPuzzle(puzzle)

    goal = solver.getFinalPuzzle(puzzleSize)
    print("Goal state:")
    helpers.debugPuzzle(goal)

    if solver.isSolvable(puzzle, goal) == False:
        helpers.exit("Puzzle is not solvable")

    solver.solve(args, puzzle, goal)

if __name__ == "__main__":
    argsParser = argparse.ArgumentParser(description='N-puzzle solver using A* or IDA algorithm')

    argsParser.add_argument('--algorithm', action='store', choices=['a', 'ida'], help='Specify the algorithm to solve the puzzle between A* and IDA*')
    argsParser.add_argument('--heuristic', action='store', choices=['misplacedTiles', 'manhattan', 'linearConflicts'], help='Specify the heuristic used')

    args = argsParser.parse_args()

    main(args)