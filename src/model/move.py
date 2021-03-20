class Move:
    def __init__(self, origin_index, destination_index):
        self._origin_index = origin_index
        self._destination_index = destination_index

    @property
    def origin_index(self):
        return self._origin_index

    @property
    def destination_index(self):
        return self._destination_index

    def validate(self, test_tubes):
        return (not test_tubes[self.origin_index].is_empty() and not test_tubes[
            self.destination_index].is_full() and not test_tubes[
            self.origin_index].is_solved() and (test_tubes[self.destination_index].is_empty() or
                                                (test_tubes[self.origin_index].get_first_ball() == test_tubes[
                                                    self.destination_index].get_first_ball())))

    def execute(self, state):
        state.test_tubes[self.destination_index].insert_ball(state.test_tubes[self.origin_index].pop_ball())
