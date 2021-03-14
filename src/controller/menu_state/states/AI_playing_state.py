import itertools
from copy import copy

import pygame

from src.controller.AI.node import Node
from src.controller.menu_state.states.playing_state import PlayingState
from src.controller.menu_state.utils.utils import is_move_possible, move_ball
from src.model.move import Move


class AIPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

        tubes = [copy(tube) for tube in self.model.test_tubes]

        self.plays = list(itertools.permutations([n for n in range(len(tubes))], 2))

        self._current_node = Node([copy(tube) for tube in tubes], None, 0, None)

        self._queue = [self._current_node]

        self._visited = {self._current_node}

    def run(self):
        run = True
        while run and self.queue:

            if self.is_solved(self.current_node.test_tubes):
                break

            for play in self.plays:

                curr_move = Move(play[0], play[1])

                if is_move_possible(self.current_node.test_tubes[play[0]], self.current_node.test_tubes[play[1]]):

                    aux = [copy(tube) for tube in self.current_node.test_tubes]
                    move_ball(aux[play[0]], aux[play[1]])
                    child = Node(aux, self.current_node, self.current_node.depth + 1, curr_move)

                    if child not in self.queue:
                        self.exec(child)

            print(len(self.queue))

            self.current_node = self.queue.pop(0)
            self.visited.add(self.current_node)

        print(len(self.visited))

        pygame.quit()

    # Template Methods
    def exec(self, child):
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

    def is_solved(self, tubes):
        for tube in tubes:
            if not tube.is_solved():
                return False
        return True
