import sys
import helpers
import solver

def main():
    puzzleSize = getPuzzleSize()
    print("Puzzle size: " + str(puzzleSize))
    print("Initial state:")

    puzzle = [[]] * puzzleSize

    for i, line in enumerate(sys.stdin):
        puzzle[i] = list(map(int, filterCommentFromLine(line).split()))

    helpers.debugPuzzle(puzzle)

    if solver.isSolvable(puzzle) == False:
        helpers.exit("Puzzle is not solvable")

    finalState = solver.getFinalPuzzle(puzzleSize)

    print("Goal state:")

    helpers.debugPuzzle(finalState)

    solver.startSolving(puzzle, finalState)

def filterCommentFromLine(line):
    commentIndex = line.find("#")
    if (commentIndex > -1):
        line = line[0:commentIndex]
    return line.strip()

def getPuzzleSize():
    puzzleSize = 0
    for line in sys.stdin:
        line = filterCommentFromLine(line)
        if (line == ""):
            continue
        lineSplit = line.split(" ")
        if (len(lineSplit) != 1 or not helpers.str_isInt(lineSplit[0])):
            helpers.exit("The first line must be single int representing the puzzle size.")
        puzzleSize = int(lineSplit[0])
        if (puzzleSize < 3):
            helpers.exit("The puzzle size must be at least of 3")
        break
    if (puzzleSize == None):
        print("You must enter a puzzle size.")
    return puzzleSize

if __name__ == "__main__":
    main()