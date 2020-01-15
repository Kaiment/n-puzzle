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

# Not admissible
# https://cse.sc.edu/~mgv/csce580sp15/gradPres/HanssonMayerYung1992.pdf
def linearConflicts(current, goal):
    size = len(current)
    h = manhattanDistance(current, goal)
    c = 0
#     lc = [ 0 ] * size
#     cr = 0
#
#     for row in range(size):
#         for tj in range(size):
#             cr[tj] = nbConflicts(goal[row], current[row], tj)
#             ctj = cr[tj]
#             while cr[tj] != 0:
#                 for tk in row:
#                     if  cr[tj] < nbConflicts(goal[row], current[row], tk):
#                         cr[tk] = 0
#                 cr[tj] -= ctj
#                 lc[row] += 1
#     print(lc)
#     sys.exit()


    for row in current:
        for col in range(size):
            c += nbConflicts(goal[col], row, col)
    for i in range(size):
        col = []
        res = []
        for j in range(size):
            res.append(goal[j][i])
            col.append(current[j][i])
        for i in range(size):
            c += nbConflicts(res, col, i)
    return h + (c * 2)

def getCoordinate(puzzle, nb, way):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == nb:
                if way == 'i':
                    return i
                return j