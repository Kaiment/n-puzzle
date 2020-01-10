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
