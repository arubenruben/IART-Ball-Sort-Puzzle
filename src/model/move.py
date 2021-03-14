class Move:
    def __init__(self, state, origin_test_tube_index, destination_test_tube_index):

        self.state = state
        self.origin_test_tube_index = origin_test_tube_index
        self.destination_test_tube_index = destination_test_tube_index

    def validate(self):

        if self.origin_test_tube_index == self.destination_test_tube_index:
            return False

        if self.state.test_tubes[self.origin_test_tube_index].is_empty():
            return False

        if self.state.test_tubes[self.destination_test_tube_index].is_full():
            return False

        if not self.state.test_tubes[self.origin_test_tube_index].is_empty() and \
                self.state.test_tubes[self.destination_test_tube_index].is_empty():
            return True

        if self.state.test_tubes[
            self.origin_test_tube_index].get_first_ball().color == self.state.test_tubes[
            self.destination_test_tube_index].get_first_ball().color:
            return True

        return False

    def execute(self, animation_manager):
        animation_manager.execute_move_animation(self)

    def fail(self, animation_manager):
        animation_manager.reverse_move_animation()
