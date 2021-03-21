from copy import copy

from src.controller.AI.node import Node
from src.controller.menu_state.states.AI_playing_state import AIPlayingState
from src.model.move import Move


class DFS(AIPlayingState):
    def __init__(self, game, model, max_depth=None):
        super().__init__(game, model)
        self._max_depth = max_depth

    def exec(self, current_iteration=None):

        if self._max_depth is not None and current_iteration is not None and current_iteration > self._max_depth:
            return

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

    def evaluate(self, node_list):
        for node in node_list:
            node.cost = 1
