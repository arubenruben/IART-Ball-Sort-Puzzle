class Node:
    def __init__(self, state, parent, depth, operator):
        self._state = state
        self._parent = parent
        self._depth = depth
        self._operator = operator
        self._g = depth
        self._h = None

    def __eq__(self, other):

        other_indexes_used = []

        for i in range(len(self.state.test_tubes)):
            for j in range(len(other.state.test_tubes)):

                if j in other_indexes_used:
                    continue

                if len(self.state.test_tubes[i]._balls) != len(other.state.test_tubes[j]._balls):
                    continue

                if len(self.state.test_tubes[i]._balls) == 0:
                    other_indexes_used.append(j)
                    continue

                for k in range(len(self.state.test_tubes[i]._balls)):
                    if self.state.test_tubes[i]._balls[k].value != other.state.test_tubes[j]._balls[k].value:
                        break
                    if k == len(self.state.test_tubes[i]._balls) - 1:
                        other_indexes_used.append(j)

        return len(other_indexes_used) == len(self.state.test_tubes)

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
