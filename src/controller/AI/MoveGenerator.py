import copy

from src.model.move import Move


class MoveGenerator:

    def state_expansion(self, node):
        node_list = []

        for i in range(len(node.state.test_tubes)):
            for j in range(len(node.state.test_tubes)):

                temp_move = Move(node.state.test_tubes[i], node.state.test_tubes[j])

                if temp_move.validate():
                    state_copy = node.state.copy()
                    state_copy.move(temp_move)

                    node_list.append(state_copy)

        return node_list
