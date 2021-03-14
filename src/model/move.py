class Move:
    def __init__(self, tube1idx, tube2idx):
        self._tube1idx = tube1idx
        self._tube2idx = tube2idx

    @property
    def tube1idx(self):
        return self._tube1idx

    @property
    def tube2idx(self):
        return self._tube2idx
