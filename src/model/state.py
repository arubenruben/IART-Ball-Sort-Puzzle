class State:
    def __init__(self, test_tubes):
        self._test_tubes = test_tubes
        self._raw_test_tubes = None

    @property
    def test_tubes(self):
        if self._test_tubes is not None:
            return self._test_tubes
        else:
            return self.expand()

    def expand(self):

        return self._test_tubes
