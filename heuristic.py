def manhattanDistance(current, goal):
    size = len(current)
    h = 0

    for i in range(0, size):
        for j in range(0, size):
            if current[i][j] != 0:
#                 https://fr.wikipedia.org/wiki/Distance_de_Manhattan
                h += abs(getCoordinate(goal, current[i][j], 'i') - i) + abs(getCoordinate(goal, current[i][j], 'j') - j)
    return h

def getCoordinate(puzzle, nb, way):
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] == nb:
                if way == 'i':
                    return i
                return j