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
#                 https://fr.wikipedia.org/wiki/Distance_de_Manhattan
                h += abs(getCoordinate(goal, current[i][j], 'i') - i) + abs(getCoordinate(goal, current[i][j], 'j') - j)
    return h

# Begin {Algorithm LC}
# { s is the current state}
# { L is the size of a line (row or column) in the puzzle. L = sqrt( N + 1 )
# { C(tj, ri) is the number of tiles in row ri with which tj is in conflict}
# { C(tj, ci) similarly}
# { lc(s, rj) is the number of tiles that must be removed from row rj to resolve the linear conflicts}
# { lc(s, cj) similarly}
# { md(s, ti) is the Manhattan Distance of tile ti}
# { MD(s) is the sum of the Manhattan Distances of all the tiles in s}
# { LC(s) is the minimum number of additional moves needed to resolve the linear conflicts in s}
# For each row ri in the state s
#    lc(s, ri) = 0
#    For each tile tj in ri
#       determine C(tj, ri)
#    While there is a non-zero C(tj, ri) value
#        Find tk such that there is no
#           C(tj, ri) > C(tk, ri) { As tk is the tile with the most conflicts, we choose to move it out of ri }
#        C(tk, ri) = 0
#        For every tile tj which had been in conflict with tk
#           C(tj, ri) = C(tj, ri) - 1
#        lc(s, ri) = lc(s, ri) + 1
# { Check similarly for linear conflicts in each column ci, computing lc(s, cj ). }
# LC(s) = 2[lc(s, r1) + . .. + lc(s, rL) + lc(s,ci) + . . . + lc(s, cL)]
# For each tile tj in s
#     determine md(s, tj)
# MD(s) = ms(s, t1) + ... + md(s, tn)
# h(s) = MD(s) + LC(s)

def nbConflicts(goal, current, tji):
    conflicts = 0
    tj = current[tji]

    if tj in goal:
        for tki, tk in enumerate(current):
            if tk != tj and tk != 0 and tj != 0 and tk in goal:# both tj and tk are not the same, different than 0 and are in the goal list
                if (tji > tki and goal.index(tj) < goal.index(tk)) or (tji < tki and goal.index(tj) > goal.index(tk)):# tile j is on the right of tile k and goal pos of tj is left of goal pos of tk or opposite..
                    conflicts += 1
    return conflicts

def linearConflicts(current, goal):
    size = len(current)
    h = manhattanDistance(current, goal)
    c = 0
#     lc = []
#
#     for row in size:
#         lc[row] = 0
#         for col in size:
#             while nbConflicts(goal[row], current[row], col) != 0:

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