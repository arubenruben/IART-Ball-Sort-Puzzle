import itertools
from copy import copy

import pygame

from src.controller.AI.utils import is_solved, Node, is_move_possible, move_ball
from src.controller.menu_state.states.playing_state import PlayingState
from src.model.move import Move


class AIPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

        tubes = [copy(tube) for tube in self.model.test_tubes]

        self.plays = list(itertools.permutations([n for n in range(len(tubes))], 2))

        self._current_node = Node([copy(tube) for tube in tubes], None, 0, None)

        self._queue = [self._current_node]

        self._visited = set([self._current_node])

    def run(self):

        while self.queue:

            parent = self.queue.pop(0)

            if is_solved(parent.test_tubes):
                while 1:
                    if parent.depth == 0:
                        break
                    print(parent.operator.tube1idx, parent.operator.tube2idx)
                    parent = parent.parent

                return parent
            for play in self.plays:
                curr_move = Move(play[0], play[1])
                if is_move_possible(parent.test_tubes[play[0]], parent.test_tubes[play[1]]):
                    aux = [copy(tube) for tube in parent.test_tubes]
                    move_ball(aux[play[0]], aux[play[1]])
                    child = Node(aux, parent, parent.depth + 1, curr_move)
                    if child not in self.visited:
                        self.queue.append(child)
                        print(len(self.queue))
                        self.visited.add(child)

        print(len(self.visited))

        pygame.quit()

        return None

    # Template Methods
    def exec(self, state_expansion):
        pass

    def evaluate(self, node_expansion):
        pass

    # Getters and Setters
    @property
    def queue(self):
        return self._queue

    @property
    def current_node(self):
        return self._current_node

    @current_node.setter
    def current_node(self, value):
        self._current_node = value

    @property
    def visited(self):
        return self._visited
