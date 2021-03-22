import math


class Node:
    def __init__(self, state, parent, depth, operator):
        self._state = state
        self._parent = parent
        self._depth = depth
        self._operator = operator
        self._g = depth
        self._h = None

    def __eq__(self, other):

        test_tube_duplication_aux = []

        for test_tube in self.state.test_tubes:
            test_tube_duplication_aux.append(test_tube)

        for other_test_tube in other.state.test_tubes:

            for self_test_tube in test_tube_duplication_aux:
                if self_test_tube == other_test_tube:
                    test_tube_duplication_aux.remove(self_test_tube)
                    break

        return len(test_tube_duplication_aux) == 0

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
