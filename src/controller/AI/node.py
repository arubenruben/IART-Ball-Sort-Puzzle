class Node:
    def __init__(self, state, parent, operator):
        self._state = state
        self._parent = parent

        if parent is None:
            self._depth = 0
        else:
            self._depth = parent.depth + 1

        self._operator = operator
        self._cost = None

    @property
    def state(self):
        return self._state

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
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    def __eq__(self, other):
        return self.state == other.state
