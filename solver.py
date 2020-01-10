import sys

import helpers
import heuristic
import puzzle

def getFinalPuzzle(size):
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

#see https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
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
    if size % 2 == 0:
        i = heuristic.getCoordinate(puzzle, 0, 'x')
        if inversions % 2 == 0 and i % 2 == 0:
            return True
        elif inversions % 2 == 1 and i % 2 == 1:
            return True
    elif inversions % 2 == 1:
        return True
    return False

# maybe we could try to order our stack when we push into it...
def getBestNode(stack):
    best = stack[0]
    for node in stack:
        if node.h < best.h:
            best = node
    return best

def startSolving(initialState, goalState):
    opened = []
    closed = []

    current = puzzle.Puzzle(initialState, goalState, 0)
    opened.append(current)

    while len(opened) > 0:
        current = getBestNode(opened)

        if current.puzzle == goalState:
            traceRoute(current)
        opened.remove(current)
        for n in current.getNeighbours():
            neighbour = puzzle.Puzzle(n, goalState, current.g + 1)
            neighbour.parent = current

            if neighbour.puzzle in closed: # or in opened with lower cost ?
                continue
            opened.append(neighbour)
        closed.append(current.puzzle)
    helpers.exit("no solution found")

def traceRoute(node):
    final = []
    print("\nA solution has been found in "+str(node.g)+" move(s)")

    while node != None:
        final.append(node)
        node = node.parent

    while len(final):
        final.pop().print()
    sys.exit()