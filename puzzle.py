import copy

import heuristic
import helpers

class Puzzle:
    def __init__(self, args, puzzle, goal, g):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.goal = goal
        self.g = g
        self.h = 0
        self.f = 0
        self.heuristic = args.heuristic
        self.searchType = args.search
        self.parent = None
        self.neighbours = []

    def __repr__(self):
        string = '\ng: '+str(self.g)+', h: '+str(self.h)+', f: '+str(self.f)+'\n'
        for row in self.puzzle:
            string += str(row)+'\n'
        return string


    def compute(self):
        if self.searchType == 'uniform':
            self.f = self.g
        else:
            if self.heuristic == 'linearConflicts':
                self.h = heuristic.linearConflicts(self.puzzle, self.goal)
            elif self.heuristic == 'misplacedTiles':
                self.h = heuristic.misplacedTiles(self.puzzle, self.goal)
            else:
                self.h = heuristic.manhattanDistance(self.puzzle, self.goal)
            if self.searchType == 'greedy':
                self.f = self.h
            else:
                self.f = self.g + self.h


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

