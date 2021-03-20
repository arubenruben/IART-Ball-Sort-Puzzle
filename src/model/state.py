class State:
    def __init__(self, test_tubes):
        self._test_tubes = test_tubes

    @property
    def test_tubes(self):
        return self._test_tubes
