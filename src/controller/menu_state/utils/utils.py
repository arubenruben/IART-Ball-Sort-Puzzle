def move_ball(tube1, tube2):
    tube2.balls.append(tube1.balls.pop())


def is_move_possible(tube1, tube2):
    return (not tube1.isEmpty() and not tube2.isFull() and not is_tube_solved(tube1)
            and (tube2.isEmpty() or is_same_color(tube1.getFirstBall(), tube2.getFirstBall())))


def is_tube_solved(tube):
    return False if len(set(tube.balls)) > 1 or len(tube.balls) == 1 else True


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
        return self.test_tubes == other.test_tubes

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
