def getFinalPuzzleSize(size):
    if not isinstance(size, int) or size < 2:
        return None

    puzzle = [0] * size
    i = 0
    j = 0
    k = 1

    for x in range(0, size):
        puzzle[x] = [0] * size

    while k < size * size:
        while j < (size - 1) and puzzle[i][j + 1] == 0:
            puzzle[i][j] = k
            j += 1
            k += 1
        while i < size - 1 and puzzle[i + 1][j] == 0:
            puzzle[i][j] = k
            i += 1
            k += 1
        while j > 0 and puzzle[i][j - 1] == 0:
            puzzle[i][j] = k
            j -= 1
            k += 1
        while i > 0 and puzzle[i - 1][j] == 0:
            puzzle[i][j] = k
            i -= 1
            k += 1

    return puzzle

def isSolvable(puzzle):
    size = len(puzzle)
    numbers = [0] * ((size * size) - 1)
    k = 0
    inversions = 0

    for i in range(0, size):
        for j in range(0, size):
            if puzzle[i][j] != 0:
                numbers[k] = puzzle[i][j]
                k += 1

    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if j > i and numbers[i] > numbers[j]:
                inversions += 1

    # even => not solvable
    if inversions % 2 == 0:
        return False
    return True

