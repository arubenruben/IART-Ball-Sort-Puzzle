from copy import copy

import pygame

from src.controller.AI.move_generator import MoveGenerator
from src.controller.AI.node import Node
from src.controller.menu_state.states.playing_state import PlayingState

from src.model.move import Move
from src.model.state import State


class AIPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)
        self.move_generator = MoveGenerator(len(model.state.test_tubes))

        self._current_node = Node(model.state.clone(), None, 0, None)

        self._queue = [self._current_node]

        self._visited = {self._current_node}

    def run(self):
        run = True
        while run and self.queue:

            if self.is_solved(self.current_node.state.test_tubes):
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for play in self.move_generator.plays:

                curr_move = Move(play[0], play[1])

                if curr_move.validate(self.current_node.state.test_tubes):

                    state_clone = self.current_node.state.clone()

                    curr_move.execute(state_clone)

                    child = Node(state_clone, self.current_node, self.current_node.depth + 1, curr_move)

                    if child not in self.queue and child not in self.visited:
                        self.exec(child)

            self.current_node = self.queue.pop(0)
            self.visited.add(self.current_node)
            print(len(self.queue))

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
