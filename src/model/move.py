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

    def validate(self, state):

        if state.test_tubes[self.origin_index].is_empty():
            return False

        if state.test_tubes[self.destination_index].is_full():
            return False

        if state.test_tubes[self.origin_index].is_solved():
            return False

        if state.test_tubes[self.destination_index].is_empty():
            return True

        if state.test_tubes[self.origin_index].get_first_ball().value != state.test_tubes[
            self.destination_index].get_first_ball().value:
            return False

        return True

    def execute(self, state):
        state.test_tubes[self.destination_index].insert_ball(state.test_tubes[self.origin_index].pop_ball())
        state.updateRawTubes(self.destination_index,self.origin_index)