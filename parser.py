import sys
import helpers

def getPuzzle(puzzleSize):
    puzzle = []
    existingCells = set()
    for line in sys.stdin:
        line = filterCommentFromLine(line)
        if (line != ""):
            lineArray = getLineArray(line, puzzleSize, existingCells)
            puzzle.append(lineArray)
    if (len(puzzle) != puzzleSize):
        print("ERROR: There must be exactly PUZZLE_SIZE rows of integers.")
        sys.exit()
    return puzzle

def getLineArray(line, puzzleSize, existingCells):
    lineArray = []
    lineSplitted = line.split(" ")
    lineSplitted = filterEmptyString(lineSplitted)
    if (len(lineSplitted) != puzzleSize):
        print("ERROR: Every row must contain PUZZLE_SIZE integers.")
        sys.exit()
    for x in range(0, puzzleSize):
        try:
            cellValue = int(lineSplitted[x])
            if (cellValue < 0 or cellValue > puzzleSize**2 - 1):
                print("ERROR: Integers values must be in range 0 to (PUZZLE_SIZE^2 - 1).")
                sys.exit()
            if (cellValue in existingCells):
                print("ERROR: Cell value duplicate.")
                sys.exit()
            else:
                existingCells.add(cellValue)
            lineArray.append(cellValue)
        except ValueError:
            print("ERROR: Each lines must contain (PUZZLE_SIZE^2 - 1) unique integers .")
            sys.exit()
    return lineArray


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

def filterCommentFromLine(line):
    commentIndex = line.find("#")
    if (commentIndex > -1):
        line = line[0:commentIndex]
    return line.strip()

def filterEmptyString(array):
    def test(e):
        return e != ""
    return list(filter(test, array))