from src.controller.ai.heuristics.heuristic import Heuristic


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

            tube_color = tube[0][0]

            must_fail = False

            for i in range(1, len(tube[0])):

                if must_fail is not True and tube[0][i] != tube_color:
                    entropy_sum += 1
                    must_fail = True

                if must_fail is True:
                    entropy_sum += 1

        return entropy_sum
