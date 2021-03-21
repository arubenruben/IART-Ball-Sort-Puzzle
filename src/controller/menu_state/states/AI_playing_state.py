from copy import copy

import pygame

from src.controller.AI.move_generator import MoveGenerator
from src.controller.AI.node import Node
from src.controller.menu_state.states.playing_state import PlayingState

from src.model.move import Move
from src.model.state import State
from src.view.animation_managers.animation_bot_manager import AnimationBotManager


class AIPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)
        self._move_generator = MoveGenerator(len(model.state.test_tubes))

        self._starting_state = model.state.clone()

        self._current_node = Node(model.state.clone(), None, 0, None)

        self._animation_manager = AnimationBotManager()

        self._queue = []

        self._visited = [self._current_node]

    def run(self):

        result = self.exec()

        if result is False:
            return print("No solution")

        path = []
        curr_node = self.visited[len(self.visited) - 1]
        while curr_node.parent is not None:
            path.append(curr_node)
            curr_node = curr_node.parent

        path.reverse()

        self.model.state = self._starting_state.clone()

        while len(self.visited):
            self.game.view.clock.tick(self.game.view.fps)

            if not self._animation_manager.animation_pending and len(path):
                self._animation_manager.execute_move_animation(path.pop(0), self.model)
            self.model.update()
            self.model.draw(self.game.view.screen)

        print(len(self.visited))

        pygame.quit()

    # Template Methods
    def exec(self):
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
