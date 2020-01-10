import copy

import heuristic
import helpers

class Puzzle:
    def __init__(self, puzzle, goal, g):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.goal = goal
        self.g = g
        self.h = heuristic.manhattanDistance(self.puzzle, self.goal)
        self.f = g + self.h
        self.parent = None
        self.neighbours = []

    def getNeighbours(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.puzzle[i][j] == 0:
                    if i > 0:
                        neighbour = copy.deepcopy(self.puzzle)
                        neighbour[i][j] = neighbour[i - 1][j]
                        neighbour[i - 1][j] = 0
                        self.neighbours.append(neighbour)
                    if j < self.size - 1:
                        neighbour = copy.deepcopy(self.puzzle)
                        neighbour[i][j] = neighbour[i][j + 1]
                        neighbour[i][j + 1] = 0
                        self.neighbours.append(neighbour)
                    if i < self.size - 1:
                        neighbour = copy.deepcopy(self.puzzle)
                        neighbour[i][j] = neighbour[i + 1][j]
                        neighbour[i + 1][j] = 0
                        self.neighbours.append(neighbour)
                    if j > 0:
                        neighbour = copy.deepcopy(self.puzzle)
                        neighbour[i][j] = neighbour[i][j - 1]
                        neighbour[i][j - 1] = 0
                        self.neighbours.append(neighbour)
        return self.neighbours

    def print(self):
        print('\ng: '+str(self.g)+', h: '+str(self.h)+', f: '+str(self.f))
        helpers.debugPuzzle(self.puzzle)

