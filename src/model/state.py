from model.elements.test_tube import TestTube
from model.utils.raw_ball_converter import convert_raw_matrix_to_balls


class State:
    def __init__(self, test_tubes):
        self._test_tubes = test_tubes
        self._raw_test_tubes = None

    @property
    def test_tubes(self):
        if self._test_tubes is None and self._raw_test_tubes is not None:
            self.expand()

        return self._test_tubes

    @property
    def raw_test_tubes(self):
        if self._raw_test_tubes is None:
            self.expand()

        return self._raw_test_tubes

    def expand(self):
        self._test_tubes = []
        for raw_test_tube in self._raw_test_tubes:
            self._test_tubes.append(
                TestTube(convert_raw_matrix_to_balls(raw_test_tube[0], raw_test_tube[1]), raw_test_tube[1]))

    def clone(self):
        raw_tubes = []
        clone = State(None)

        for test_tube in self.test_tubes:
            raw_tubes.append((test_tube.get_raw_balls(), test_tube.rect.copy()))

        clone._raw_test_tubes = raw_tubes

        return clone

    def update_raw_tubes(self, destination, origin):
        moved_color = self._raw_test_tubes[origin][0].pop()
        self._raw_test_tubes[destination][0].append(moved_color)
