class Node:
    def __init__(self, state, parent, depth, operator):
        self._state = state
        self._parent = parent
        self._depth = depth
        self._operator = operator

    def __eq__(self, other):
        for i in range(len(self.state.test_tubes)):
            if len(self.state.test_tubes[i]._balls) != len(other.state.test_tubes[i]._balls):
                return False

            for j in range(len(self.state.test_tubes[i]._balls)):
                if self.state.test_tubes[i]._balls[j].value != other.state.test_tubes[i]._balls[j].value:
                    return False

        return True

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

    def clone(self):
        return Node(self.state.clone(), self.parent, self.depth, self.operator)
