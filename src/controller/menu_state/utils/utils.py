# Using Aux Set to remove duplicates and if the number of balls is just 1 or 0 is finished
def is_tube_solved(tube):
    if len(set(tube.balls)) > 1 or len(tube.balls) == 1:
        return False
    else:
        return True


def is_solved(tubes):
    for tube in tubes:
        if not is_tube_solved(tube):
            return False
    return True


def is_same_color(ball1, ball2):
    return ball1.color == ball2.color


class Node:
    def __init__(self, test_tubes, parent, depth, operator):
        self._test_tubes = test_tubes  # Game State
        self._parent = parent
        self._depth = depth
        self._operator = operator

    def __eq__(self, other):
        return self.test_tubes == other.state

    def __hash__(self):
        return hash(tuple(self.test_tubes))

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
