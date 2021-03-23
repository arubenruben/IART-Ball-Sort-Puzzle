from src.controller.AI.heuristics.heuristic import Heuristic


class TabooSearchHeuristic(Heuristic):
    def evaluate(self, node):
        tubes = node.state.raw_test_tubes

        total = 0

        for tube in tubes:

            if len(tube[0]) == 0:
                total += 10
                continue

            tube_color = tube[0][0]
            total += 5

            for i in range(1, len(tube[0])):

                if tube[0][i] == tube_color:
                    total += 5
                else:
                    break

        return total

