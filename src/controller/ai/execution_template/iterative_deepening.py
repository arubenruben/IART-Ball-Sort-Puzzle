import pygame

from controller.ai.node import Node
from controller.menu_state.states.ai_playing_state import AIPlayingState
from model.headers.bot_searching_header import BotSearchingHeader


class IterativeDeepening(AIPlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

        self._staring_header = BotSearchingHeader("Iterative Deepening")
        self.model.header = self._staring_header

    def run(self):
        run = True
        max_depth = 1
        solved = False

        while run:

            self._queue = []

            self._current_node = Node(self._starting_state.clone(), None, 0, None)

            self._visited = [self._current_node]

            current_depth = 1

            while True:

                self.update_and_draw_state()

                if self.is_solved(self.current_node.state.test_tubes):
                    solved = True
                    break

                if current_depth > max_depth:
                    break

                self.node_expansion()

                if len(self.queue) > 0:
                    self.current_node = self.queue.pop()
                    self.visited.append(self.current_node)
                else:
                    return self.change_to_state_defeat()

                current_depth += 1

            if solved is False:
                max_depth += 1
            else:
                self.draw_solution()
                if self.model.next_level():
                    self.reset()
                    return self.run()
                else:
                    pygame.quit()
                    return

    def exec(self, child):
        self.queue.append(child)
