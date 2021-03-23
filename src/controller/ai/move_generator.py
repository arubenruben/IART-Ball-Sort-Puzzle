import itertools


class MoveGenerator:
    def __init__(self, number_tubes):
        self._plays = list(itertools.permutations([n for n in range(number_tubes)], 2))

    @property
    def plays(self):
        return self._plays
