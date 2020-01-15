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

def countInversions(puzzle, goal):
    res = 0
    for i in range(len(puzzle) - 1):
        for j in range(i + 1, len(puzzle)):
                ti = puzzle[i]
                tj = puzzle[j]
                if goal.index(ti) > goal.index(tj):
                    res += 1
    return res

#see https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/
def isSolvable(puzzle, goal):
    size = len(puzzle)
    puzzle = [item for sublist in puzzle for item in sublist]
    goal = [item for sublist in goal for item in sublist]

    inversions = countInversions(puzzle, goal)
    puzzleZR = puzzle.index(0) // size
    puzzleZC = puzzle.index(0) % size
    goalZR = goal.index(0) // size
    goalZC = goal.index(0) % size
    dist = abs(puzzleZR - goalZR) + abs(puzzleZC - goalZC)
    if (dist % 2 == 0 and inversions % 2 == 0) or (dist % 2 == 1 and inversions % 2 == 1):
        return True
    return False

# maybe we could try to order our stack when we push into it to improve solving time...
def getBestNode(stack):
    best = stack[0]

    for node in stack:
        if node.f < best.f:
            best = node
    return best

def openedWithLowerCost(node, opened):
    for op in opened:
        if op.puzzle == node.puzzle and op.g < node.g:
            return True
    return False

def idaStar(initialState, goalState):
    current = puzzle.Puzzle(initialState, goalState, 0)
    current.compute()
    threshold = current.h

    while True:
        res = idaSearch(current, goalState, 0, threshold)
        if res == 0:
            helpers.exit()
        if res > sys.maxsize:
            helpers.exit("no solution found")
        threshold = res

def idaSearch(current, goalState, g, threshold):
    current.compute()

    if current.f > threshold:
        return current.f
    if current.h == 0:
        traceRoute(current)
        return 0
    min = sys.maxsize
    for n in current.getNeighbours():
        neighbour = puzzle.Puzzle(n, goalState, g + 1)
        neighbour.parent = current
        res = idaSearch(neighbour, goalState, g + 1, threshold)
        if res == 0:
            traceRoute(neighbour)
            return 0
        if res < min:
            min = res
    return min

def isClosed(node, closed):
    for c in closed:
        if c.puzzle == node.puzzle and c.g == node.g:
            return True
    return False

def aStar(initialState, goalState):
    opened = []
    closed = []

    current = puzzle.Puzzle(initialState, goalState, 0)
    current.compute()
    opened.append(current)

    h = current.h

    while len(opened) > 0:
        current = getBestNode(opened)

        if current.h == 0:
            traceRoute(current)
        opened.remove(current)
        for n in current.getNeighbours():
            neighbour = puzzle.Puzzle(n, goalState, current.g + 1)
            neighbour.compute()
            neighbour.parent = current

            if isClosed(neighbour, closed) or openedWithLowerCost(neighbour, opened) == True:
                continue
            opened.append(neighbour)
        closed.append(current)
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
