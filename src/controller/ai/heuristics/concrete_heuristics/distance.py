from src.controller.ai.heuristics.heuristic import Heuristic


def count_tube_colors(tube, color):
    count = 0
    for ball in tube:
        if ball == color:
            count += 1
        else:
            break
    return count


class DistanceHeuristic(Heuristic):

    def evaluate(self, node):
        tubes = node.state.raw_test_tubes
        tube_color = {}
        empty_tubes = []

        j = -1
        for tube in tubes:

            j += 1
            if len(tube[0]) == 0:
                empty_tubes.append(j)
                continue

            curr_count = count_tube_colors(tube[0], tube[0][0])
            if tube[0][0] in tube_color.keys():
                if curr_count > tube_color[tube[0][0]][1]:
                    tube_color[tube[0][0]] = (j, curr_count)
                elif curr_count == tube_color[tube[0][0]][1]:
                    if len(tube[0]) < len(tubes[tube_color[tube[0][0]][0]][0]):
                        tube_color[tube[0][0]] = (j, curr_count)
            else:
                tube_color[tube[0][0]] = (j, curr_count)

        distance = 0
        k = -1
        for tube in tubes:
            k += 1
            # If there are less than 2 balls, a tube will always be homogenous
            if len(tube[0]) == 0:
                continue

            for i in range(len(tube[0])):
                if tube[0][i] not in tube_color.keys():
                    if len(empty_tubes) > 0:
                        distance += len(tube[0]) - i
                elif k == tube_color[tube[0][i]][0]:
                    continue
                else:
                    distance += len(tube[0]) - i
                    #distance += len(tube[0]) - i + len(tubes[tube_color[tube[0][i]][0]][0]) - tube_color[tube[0][i]][1]

        return distance
