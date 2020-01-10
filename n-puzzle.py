import sys
import helpers
import solver

def main():
    puzzleSize = getPuzzleSize()
    print("Puzzle size: " + str(puzzleSize))
    print("Rest of the input:")

    for i, line in enumerate(sys.stdin):
        print(filterCommentFromLine(line))

    finalState = solver.getFinalPuzzleSize(10)

    print("Goal state:")

    helpers.debugPuzzle(finalState)

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
            print("The first line must be single int representing the puzzle size.")
            sys.exit()
        puzzleSize = int(lineSplit[0])
        if (puzzleSize < 3):
            print("The puzzle size must be at least of 3")
            sys.exit()
        break
    if (puzzleSize == None):
        print("You must enter a puzzle size.")
    return puzzleSize

if __name__ == "__main__":
    main()