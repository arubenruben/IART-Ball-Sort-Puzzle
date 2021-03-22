class Node:
    def __init__(self, state, parent, depth, operator):
        self._state = state
        self._parent = parent
        self._depth = depth
        self._operator = operator
        self._g = depth
        self._h = None

    def __eq__(self, other):
        selfTubesClone= self.state.raw_test_tubes[:]
        otherTubesClone=other.state.raw_test_tubes[:]
        i=0
        for tube1 in list(selfTubesClone):
            j=0
            removed=False
            for tube2 in list(otherTubesClone):  
                if self.compareRawTubes(tube1[0],tube2[0]):
                    selfTubesClone.pop(i)
                    i-=1
                    otherTubesClone.pop(j)
                    removed=True
                    break
                j+=1
            if not removed:
                return False
            i+=1

        if len(selfTubesClone)==0:
            return True
        
        """for i in range(len(self.state.test_tubes)):
            if len(self.state.test_tubes[i]._balls) != len(other.state.test_tubes[i]._balls):
               return False

            for j in range(len(self.state.test_tubes[i]._balls)):
                if self.state.test_tubes[i]._balls[j].value != other.state.test_tubes[i]._balls[j].value:
                    return False

        return True"""

    @property
    def parent(self):
        return self._parent

    @property
    def depth(self):
        return self._depth

    @property
    def operator(self):
        return self._operator

    @property
    def state(self):
        return self._state

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = value

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value

    def clone(self):
        return Node(self.state.clone(), self.parent, self.depth, self.operator)

    def compareRawTubes(self,tube1,tube2):
        if len(tube1) != len(tube2):
            return False
        
        for j in range(len(tube1)):
            if tube1[j]!=tube2[j]:
                return False

        return True