def str_isInt(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def debugPuzzle(puzzle):

    size = len(puzzle)

    for i in range(0, size):
        print(' '.join(str(x).ljust(3) for x in puzzle[i]))
