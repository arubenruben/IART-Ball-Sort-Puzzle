import pygame

from src.controller.AI.MoveGenerator import MoveGenerator
from src.controller.AI.node import Node
from src.controller.AI.utils import is_solved
from src.controller.menu_state.states.playing_state import PlayingState


class AIPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)
        self._move_generator = MoveGenerator()
        self._current_node = Node(model.state, None, None)

        self._queue = [self._current_node]

        self._visited = [self._current_node]

    def run(self):
        run = True

        while run and self.current_node is not None:

            # self.game.view.clock.tick(self.game.view.fps)

            if is_solved(self.current_node.state.test_tubes):
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            potential_nodes = self._move_generator.state_expansion(self.current_node)

            self.exec(potential_nodes)

            self.current_node = self.queue.pop(0)

            self._visited.append(self.current_node)
            # self.model.draw(self.game.view.screen)

        print(len(self._visited))

        pygame.quit()

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
