import copy

from src.controller.AI.node import Node
from src.controller.menu_state.states.AI_playing_state import AIPlayingState


class BFSAI(AIPlayingState):
    def exec(self, state_expansion):
        node_list = []
        # Todo:Operator What information is usefull?

        for state in state_expansion:
            already_visited = False

            for previous_node in self.visited:
                if state == previous_node.state:
                    already_visited = True
                    break

            if not already_visited:
                node_list.append(Node(state, self.current_node, "move"))

        self.evaluate(node_list)

        self._queue = self._queue + node_list

    def evaluate(self, node_list):
        for node in node_list:
            node.cost = 1
