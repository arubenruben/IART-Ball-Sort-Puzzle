class Node:
    def __init__(self, test_tubes, parent, depth, operator):
        # Game State
        self._test_tubes = test_tubes
        self._parent = parent
        self._depth = depth
        self._operator = operator

    def __eq__(self, other):
        return self.test_tubes == other.test_tubes

    @property
    def test_tubes(self):
        return self._test_tubes

    def __hash__(self):
        return super().__hash__()

    @property
    def parent(self):
        return self._parent

    @property
    def depth(self):
        return self._depth

    @property
    def operator(self):
        return self._operator
