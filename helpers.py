import sys

def str_isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def exit(str):
    print("\n" + str)
    sys.exit()

def debugPuzzle(puzzle):
    size = len(puzzle)

    for i in range(0, size):
        print(' '.join(str(x).ljust(2) for x in puzzle[i]))
