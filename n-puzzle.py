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

def filterEmptyString(array):
    def test(e):
        return e != ""
    return list(filter(test, array))

def getPuzzle(puzzleSize):
    puzzle = [[-1 for i in range(0, puzzleSize)] for j in range(0, puzzleSize)]
    puzzleDict = {}
    for y, line in enumerate(sys.stdin):
        line = filterCommentFromLine(line)
        if (line != ""):
            lineSplitted = line.split(" ")
            lineSplitted = filterEmptyString(lineSplitted)
            if (len(lineSplitted) != puzzleSize):
                print("ERROR: Every row must strictly be of the puzzle size.")
                sys.exit()
            for x in range(0, puzzleSize):
                try:
                    slot = int(lineSplitted[x])
                    if (slot < 0 or slot > puzzleSize**2 - 1):
                        print("ERROR: Integers values must be from 0 to [puzzle size]^2 - 1.")
                    if (slot in puzzleDict.keys()):
                        print("ERROR: Cell value duplicate.")
                        sys.exit()
                    else:
                        puzzleDict[slot] = True
                    puzzle[y][x] = slot
                except ValueError:
                    print("ERROR: Each lines must be composed of unique integers [puzzle size]^2 - 1.")
                    sys.exit()
    if (len(puzzle) != puzzleSize):
        print("ERROR: There must be exactly [puzzle size] rows of integers.")
    return puzzle

def getPuzzleSize():
    puzzleSize = 0
    for line in sys.stdin:
        line = filterCommentFromLine(line)
        if (line == ""):
            continue
        lineSplit = line.split(" ")
        if (len(lineSplit) != 1 or not helpers.str_isInt(lineSplit[0])):
            print("ERROR: The first line must be single int representing the puzzle size.")
            sys.exit()
        puzzleSize = int(lineSplit[0])
        if (puzzleSize < 2):
            print("ERROR: The puzzle size must be at least of 2")
            sys.exit()
        break
    if (puzzleSize == None):
        print("ERROR: You must enter a puzzle size.")
    return puzzleSize

if __name__ == "__main__":
    main()