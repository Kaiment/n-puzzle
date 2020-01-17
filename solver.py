import sys
import time

import helpers
import heuristic
import puzzle
import IndexedPriorityQueue

def fillFinalPuzzle(size):
    puzzle = [0] * size
    k = 1

    for x in range(size):
        puzzle[x] = [0] * size
        for y in range(size):
            puzzle[x][y] = k
            k += 1

    puzzle[x][y] = 0
    return puzzle

def snakeFinalPuzzle(size):
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

def getFinalPuzzle(size, type):
    if type == 'fill':
        return fillFinalPuzzle(size)
    return snakeFinalPuzzle(size)

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
def isSolvable(puzzle, goal, arg):
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

def solve(args, initialState, goalState):
    global arguments
    global startTime
    arguments = args
    startTime = time.time()

    if args.algorithm == 'a':
        aStar(initialState, goalState)
    else:
        idaStar(initialState, goalState)

def openedWithLowerCost(node, opened):
    for op in opened:
        if op.puzzle == node.puzzle and op.g < node.g:
            return True
    return False


def idaStar(initialState, goalState):
    current = puzzle.Puzzle(arguments, initialState, goalState, 0)
    current.compute()
    threshold = current.f

    while True:
        res = idaSearch(current, goalState, 0, threshold)
        if res == 0:
            helpers.exit("")
        if res > sys.maxsize:
            helpers.exit("no solution found")
        threshold = res

def idaSearch(current, goalState, g, threshold):
    current.compute()

    current.print()

    if current.f > threshold:
        return current.f
    if current.puzzle == goalState:
        traceRoute(current)
        return 0
    min = sys.maxsize
    for n in current.getNeighbours():
        neighbour = puzzle.Puzzle(arguments, n, goalState, g + 1)
        neighbour.parent = current
        res = idaSearch(neighbour, goalState, g + 1, threshold)
        if res == 0:
            traceRoute(neighbour)
            return 0
        if res < min:
            min = res
    return min

def openedWithLowerCost(node, opened):
    for op in opened:
        if op.puzzle == node.puzzle and op.g < node.g:
            return True
    return False

def isClosed(node, closed):
    for c in closed:
        if c.puzzle == node.puzzle and c.f == node.f:
            return True
    return False

def aStar(initialState, goalState):
    #opened = []
    closed = set() # with set
    openedIPQ = IndexedPriorityQueue.IndexedPriorityQueue()

    currentIPQ = puzzle.Puzzle(initialState, goalState, 0)
    currentIPQ.compute()
    #opened.append(current)

    # test IPQ
    openedIPQ.append(currentIPQ)

    while len(openedIPQ.opened) > 0:
        #current = getBestNode(opened)

        #print(openedIPQ)
        currentIPQ = openedIPQ.pop()
        if currentIPQ.h == 0:
            traceRoute(currentIPQ)
        #opened.remove(current)
        for n in currentIPQ.getNeighbours():
            neighbour = puzzle.Puzzle(n, goalState, currentIPQ.g + 1)
            neighbour.compute()
            neighbour.parent = currentIPQ

            if hashPuzzle(neighbour.puzzle, neighbour.g) in closed or openedWithLowerCost(neighbour, openedIPQ.opened):
                continue
            openedIPQ.append(neighbour)

            # IPQ TEST
            openedIPQ.append(neighbour)

        closed.add(hashPuzzle(currentIPQ.puzzle, currentIPQ.g))


    helpers.exit("no solution found")

def hashPuzzle(puzzle, g):
    hashValue = ""
    for row in puzzle:
        hashValue += "".join(map(str, row))
    hashValue += str(g)
    return hashValue

def traceRoute(node):
    endTime = time.time()
    timeElapsed = endTime - startTime

    final = []
    print("\nA solution has been found in "+str(node.g)+" move(s) and "+str(round(timeElapsed, 3))+" s")

    while node != None:
        final.append(node)
        node = node.parent

    while len(final):
        final.pop().print()
    sys.exit()
