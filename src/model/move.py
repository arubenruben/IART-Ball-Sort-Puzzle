from src.controller.utils.utils import is_same_color


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

    def validate(self, test_tubes):
        return (not test_tubes[self.tube1idx].is_empty() and not test_tubes[self.tube2idx].is_full() and not test_tubes[
            self.tube1idx].is_solved() and (test_tubes[self.tube2idx].is_empty() or is_same_color(
            test_tubes[self.tube1idx].get_first_ball(),
            test_tubes[self.tube2idx].get_first_ball())))

    def execute(self, test_tubes):
        test_tubes[self.tube2idx].insert_ball(test_tubes[self.tube1idx].pop_ball())
