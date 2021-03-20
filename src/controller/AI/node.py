class Node:
    def __init__(self, test_tubes, parent, depth, operator):
        # Game State
        self._test_tubes = test_tubes
        self._parent = parent
        self._depth = depth
        self._operator = operator

    def __eq__(self, other):
        for i in range(len(self.test_tubes)):
            if len(self.test_tubes[i]._balls) != len(other.test_tubes[i]._balls):
                return False

            for j in range(len(self.test_tubes[i]._balls)):
                if self.test_tubes[i]._balls[j].value != self.test_tubes[i]._balls[j].value:
                    return False
        return True

    def __hash__(self):
        return super().__hash__()

    @property
    def test_tubes(self):
        return self._test_tubes

    @property
    def parent(self):
        return self._parent

    @property
    def depth(self):
        return self._depth

    @property
    def operator(self):
        return self._operator
