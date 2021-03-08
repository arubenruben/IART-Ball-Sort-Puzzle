import pygame
import copy

from src.model.elements.test_tube import TestTube


def get_simplified_state(tubes):
    ret = []
    for tube in tubes:
        ret.append(tube.balls)
    return ret


def is_solved(tubes):
    for tube in tubes:
        if len(set(tube)) > 1:
            return False
    return True


def is_move_possible(tube1, tube2):
    return len(tube1) != 0 and len(tube2) < 4 and (len(tube2) == 0 or tube1[-1] == tube2[-1])


def move_ball(tube1, tube2):
    if is_move_possible(tube1, tube2):
        new_tube1 = copy.deepcopy(tube1)
        new_tube2 = copy.deepcopy(tube2)
        new_tube2.append(new_tube1.pop())
        return new_tube1, new_tube2


class Node:
    def __init__(self, test_tubes, parent, depth, operator):
        self._test_tubes = test_tubes  # Game State
        self._parent = parent
        self._depth = depth
        self._operator = operator

    def __eq__(self, other):
        return self.test_tubes == other.test_tubes

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
