class MoveForHuman:
    def __init__(self, origin_test_tube, destination_test_tube):
        self._origin_test_tube = origin_test_tube
        self._destination_test_tube = destination_test_tube

    def validate(self):

        if not self.origin_test_tube.is_empty() and self.destination_test_tube.is_empty():
            return True

        if self.destination_test_tube.is_full():
            return False

        if self.origin_test_tube.get_first_ball().color == self.destination_test_tube.get_first_ball().color:
            return True

        return False

    def execute(self, animation_manager):
        animation_manager.execute_move_animation(self)

    def fail(self, animation_manager):
        animation_manager.reverse_move_animation()

    @property
    def origin_test_tube(self):
        return self._origin_test_tube

    @property
    def destination_test_tube(self):
        return self._destination_test_tube
