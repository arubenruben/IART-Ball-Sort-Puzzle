class Move:
    def __init__(self, origin_test_tube, destination_test_tube):
        self._origin_test_tube = origin_test_tube
        self._destination_test_tube = destination_test_tube

    def validate(self, state):
        return True

    def execute(self, state, animation_manager):
        animation_manager.execute_move_animation(self)

    @property
    def origin_test_tube(self):
        return self._origin_test_tube

    @property
    def destination_test_tube(self):
        return self._destination_test_tube
