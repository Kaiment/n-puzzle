class Index:
    def __init__(self, insertIndex):
        self.insertIndex = insertIndex
        self.count = 0

    def __repr__(self):
        return "index: "+str(self.insertIndex)+" count: "+str(self.count)

class IndexedPriorityQueue:
    def __init__(self):
        self.indexDict = {}
        self.openedDict = {}
        self.opened = []
        self.allTimeOpened = 0
        self.maxSameTimeOpened = 0

    def __repr__(self):
        return str(self.indexDict)+"\n"+str(self.opened)

    def getOpenedLength(self):
        return len(self.opened)

    def getInsertionIndex(self, f):
        def computeInsertIndex(f):
            insertIndex = 0
            for idxF in self.indexDict:
                if idxF < f:
                    insertIndex += self.indexDict[idxF].count
            return insertIndex

        if f in self.indexDict:
            return self.indexDict[f].insertIndex
        else:
            self.indexDict[f] = Index(computeInsertIndex(f))
            return self.indexDict[f].insertIndex

    def append(self, puzzle):
        insertionIndex = self.getInsertionIndex(puzzle.f)
        self.updateMaxSameTimeOpened()
        if insertionIndex == self.getOpenedLength():
            self.opened.append(puzzle)
            #print("append "+str(puzzle.f)+" at the end")
        else:
            self.opened.insert(insertionIndex, puzzle)
            #print("append "+str(puzzle.f)+" at index "+str(insertionIndex))
        self.appendOpenedDict(puzzle)
        self.indexDict[puzzle.f].count += 1
        self.incrementIndexOfGreaterF(puzzle.f)
        self.allTimeOpened += 1
        return 0

    def appendOpenedDict(self, puzzle):
        if puzzle.g in self.openedDict:
            self.openedDict[puzzle.g].add(self.hashPuzzle(puzzle.puzzle))
        else:
            self.openedDict[puzzle.g] = set([self.hashPuzzle(puzzle.puzzle)])

    def hashPuzzle(self, puzzle):
        hashValue = ""
        for row in puzzle:
            hashValue += "".join(map(str, row))
        return hashValue

    def pop(self):
        puzzle = self.opened.pop(0)
        self.popOpenedDict(puzzle)
        #print("popped "+str(puzzle.f)+" at index 0")
        self.indexDict[puzzle.f].count -= 1
        if self.indexDict[puzzle.f].count < 1:
            del self.indexDict[puzzle.f]
        self.decrementIndexOfGreaterF(puzzle.f)
        return puzzle

    def popOpenedDict(self, puzzle):
        if puzzle.g in self.openedDict:
            self.openedDict[puzzle.g].remove(self.hashPuzzle(puzzle.puzzle))
            if len(self.openedDict) < 1:
                del self.openedDict[puzzle.g]
        
    def incrementIndexOfGreaterF(self, f):
        for idxF in self.indexDict:
            if idxF > f:
                self.indexDict[idxF].insertIndex += 1

    def decrementIndexOfGreaterF(self, f):
        for idxF in self.indexDict:
            if idxF > f:
                self.indexDict[idxF].insertIndex -= 1

    def updateMaxSameTimeOpened(self):
        nbOpened = self.getNbOpened()
        if nbOpened > self.maxSameTimeOpened:
            self.maxSameTimeOpened = nbOpened

    def getNbOpened(self):
        nbOpened = 0
        for op in self.indexDict:
            nbOpened += self.indexDict[op].count
        return nbOpened

    def gotOpenedWithLowerCost(self, puzzle):
        puzzleHash = self.hashPuzzle(puzzle.puzzle)
        for p in self.openedDict:
            if p <= puzzle.g:
                if puzzleHash in self.openedDict[p]:
                    return True
        return False