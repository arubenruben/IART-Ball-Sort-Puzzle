from src.model.elements.test_tube import TestTube


class State:
    def __init__(self, test_tubes):
        self._test_tubes = test_tubes

    def copy(self):
        test_tube_copy_list = []

        for test_tube in self._test_tubes:
            test_tube_copy_list.append(TestTube(test_tube.raw_ball_list(), test_tube.rect.copy()))

        return State(test_tube_copy_list)

    def move(self, move):
        extracted_ball = self.test_tubes[move.origin_test_tube_index].balls.pop(
            len(self.test_tubes[move.origin_test_tube_index].balls) - 1)
        self.test_tubes[move.destination_test_tube_index].balls.append(extracted_ball)

    @property
    def test_tubes(self):
        return self._test_tubes

    def __eq__(self, other):
        for i in range(len(self.test_tubes)):
            if len(self.test_tubes[i].balls) != len(other.test_tubes[i].balls):
                return False
            for j in range(len(self.test_tubes[i].balls)):
                if self.test_tubes[i].balls[j].value != other.test_tubes[i].balls[j].value:
                    return False

        return True
