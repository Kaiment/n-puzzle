def misplacedTiles(current, goal):
    size = len(current)
    h = 0

    for i in range(size):
        for j in range(size):
            if current[i][j] != 0 and current[i][j] != goal[i][j]:
                h += 1
    return h

def manhattanDistance(current, goal):
    size = len(current)
    h = 0

    for i in range(size):
        for j in range(size):
            if current[i][j] != 0:
                h += abs(getCoordinate(goal, current[i][j], 'i') - i) + abs(getCoordinate(goal, current[i][j], 'j') - j)
    return h

def nbConflicts(goal, current, tji):
    conflicts = 0
    tj = current[tji]

    if tj in goal:
        for tki, tk in enumerate(current):
            if tk != tj and tk != 0 and tj != 0 and tk in goal:# both tj and tk are not the same, different than 0 and are in the goal list
                if (tji > tki and goal.index(tj) < goal.index(tk)) or (tji < tki and goal.index(tj) > goal.index(tk)):# tile j is on the right of tile k and goal pos of tj is left of goal pos of tk or opposite..
                    conflicts += 1
    return conflicts

def rowStillHasConflicts(list):
    for el in list:
        if el > 0:
            return True
    return False

def getMostConflicts(list):
    best = 0
    for index, el in enumerate(list):
        if el > best:
            best = index
    return best

def getConflicts(goal, current, tji):
    conflicts = []
    tj = current[tji]

    if tj in goal:
        for tki, tk in enumerate(current):
            if tk != tj and tk != 0 and tj != 0 and tk in goal:# both tj and tk are not the same, different than 0 and are in the goal list
                if (tji > tki and goal.index(tj) < goal.index(tk)) or (tji < tki and goal.index(tj) > goal.index(tk)):# tile j is on the right of tile k and goal pos of tj is left of goal pos of tk or opposite..
                    conflicts.append(tki)
    return conflicts

# https://cse.sc.edu/~mgv/csce580sp15/gradPres/HanssonMayerYung1992.pdf
def linearConflicts(current, goal):
    size = len(current)
    h = manhattanDistance(current, goal)
    lc = 0
    lcr = [ 0 ] * size # linear conflicts row
    crn = [ 0 ] * size # conflicts row number
    lcc = [ 0 ] * size
    ccn = [ 0 ] * size

    for row in range(size):
        for tj in range(size):
            crn[tj] = nbConflicts(goal[row], current[row], tj)
        while rowStillHasConflicts(crn):
            tk = getMostConflicts(crn)
            crn[tk] = 0
            for tj in getConflicts(goal[row], current[row], tk):
                crn[tj] -= 1
            lc += 1
    for row in range(size):
        col = []
        res = []
        for j in range(size):
            res.append(goal[j][row])
            col.append(current[j][row])
        for tj in range(size):
            ccn[tj] = nbConflicts(res, col, tj)
        while rowStillHasConflicts(ccn):
            tk = getMostConflicts(ccn)
            ccn[tk] = 0
            for tj in getConflicts(res, col, tk):
                ccn[tj] -= 1 # pruning related conflicts by one
            lc += 1 # there is one conflict for each conflicted tile removed.

    return h + 2 * lc

def getCoordinate(puzzle, nb, way):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == nb:
                if way == 'i':
                    return i
                return j