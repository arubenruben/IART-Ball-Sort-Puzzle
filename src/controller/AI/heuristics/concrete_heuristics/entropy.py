from src.controller.AI.heuristics.heuristic import Heuristic


class EntropyHeuristic(Heuristic):

    def __init__(self):
        super().__init__()

    def evaluate(self, node):
        tubes = node.state._raw_test_tubes

        entropy_sum = 0

        for tube in tubes:

            # If there are less than 2 balls, a tube will always be homogenous
            if len(tube[0]) <= 1:
                continue

            tubeColor = tube[0][0]

            for i in range(1, len(tube[0])):

                if tube[0][i] != tubeColor:
                    entropy_sum += 1

        return entropy_sum
