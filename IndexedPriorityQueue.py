class Index:
    def __init__(self, insertIndex):
        self.insertIndex = insertIndex
        self.count = 0

    def __repr__(self):
        return "index: "+str(self.insertIndex)+" count: "+str(self.count)

class IndexedPriorityQueue:
    def __init__(self):
        self.indexDict = {}
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
        if insertionIndex == self.getOpenedLength():
            self.opened.append(puzzle)
            #print("append "+str(puzzle.f)+" at the end")
        else:
            self.opened.insert(insertionIndex, puzzle)
            #print("append "+str(puzzle.f)+" at index "+str(insertionIndex))
        self.indexDict[puzzle.f].count += 1
        self.incrementIndexOfGreaterF(puzzle.f)
        self.allTimeOpened += 1
        return 0

    def pop(self):
        puzzle = self.opened.pop(0)
        #print("popped "+str(puzzle.f)+" at index 0")
        self.indexDict[puzzle.f].count -= 1
        if self.indexDict[puzzle.f].count < 1:
            del self.indexDict[puzzle.f]
        self.decrementIndexOfGreaterF(puzzle.f)
        return puzzle
        
    def incrementIndexOfGreaterF(self, f):
        for idxF in self.indexDict:
            if idxF > f:
                self.indexDict[idxF].insertIndex += 1

    def decrementIndexOfGreaterF(self, f):
        for idxF in self.indexDict:
            if idxF > f:
                self.indexDict[idxF].insertIndex -= 1

    def gotOpenedWithLowerCost(self):
        return 0
    