from src.controller.AI.heuristics.heuristic import Heuristic


class DistanceHeuristic(Heuristic):

    def evaluate(self, node):
        tubes = node.state.raw_test_tubes

        distance = 0

        for tube in tubes:

            # If there are less than 2 balls, a tube will always be homogenous
            if len(tube[0]) <= 1:
                continue

            tubeColor = tube[0][0]

            for i in range(1, len(tube[0])):
                if tube[0][i] != tubeColor:
                    pass
        pass
