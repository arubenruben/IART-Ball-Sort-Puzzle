from copy import copy

import pygame

from src.controller.AI.execution_template.dfs import DFS
from src.controller.AI.node import Node
from src.controller.menu_state.states.AI_playing_state import AIPlayingState
from src.model.move import Move


class IterativeDeepening(AIPlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

    def exec(self):
        run = True
        max_depth = 1

        while run:
            self._queue = []
            self._visited = [self._current_node]

            self._current_node = self._starting_state.clone()

            self.model.state = self._current_node.state

            current_depth = 1

            while True:

                self.game.view.clock.tick(self.game.view.fps)

                if self.is_solved(self.current_node.state.test_tubes):
                    return

                if current_depth > max_depth:
                    break

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        break

                for play in self._move_generator.plays:

                    curr_move = Move(play[0], play[1])

                    if curr_move.validate(self.current_node.state):

                        state_clone = self.current_node.state.clone()

                        curr_move.execute(state_clone)

                        child = Node(state_clone, self.current_node.clone(), self.current_node.depth + 1,
                                     copy(curr_move))

                        unique = True
                        for visited_node in self.visited:
                            if child == visited_node:
                                unique = False
                                break

                        for node_in_queue in self.queue:
                            if child == node_in_queue:
                                unique = False
                                break

                        if unique:
                            self.queue.insert(0, child)

                self.current_node = self.queue.pop(0)
                self.visited.append(self.current_node)
                self.model.state = self.current_node.state

                current_depth += 1

                self.model.update()
                self.model.draw(self.game.view.screen)

            max_depth += 1
