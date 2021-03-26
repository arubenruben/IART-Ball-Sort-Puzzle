from src.controller.AI.heuristics.heuristic import Heuristic


class TabooSearchHeuristic(Heuristic):
    def evaluate(self, node):
        tubes = node.state.raw_test_tubes

        num_empty_tubes = 0
        total = 0

        for tube in tubes:

            if len(tube[0]) == 0:
                num_empty_tubes += 1
                continue

            tube_color = tube[0][0]

            for i in range(1, len(tube[0])):

                if tube[0][i] != tube_color:
                    total += 2 * (len(tube[0]) - i)
                    break
        total += num_empty_tubes
        return total

