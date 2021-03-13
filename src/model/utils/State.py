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
        extracted_ball = move.origin_test_tube.balls.pop()
        move.destination_test_tube.balls.append(extracted_ball)

    @property
    def test_tubes(self):
        return self._test_tubes

    def __eq__(self, other):
        return self.test_tubes == other.test_tubes
