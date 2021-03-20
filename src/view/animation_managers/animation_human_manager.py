from src.model.move_for_human import MoveForHuman
from src.view.animation_managers.animation_bot_manager import AnimationManager


# States: Down. Up. Moving_UP. Moving_DOWN Moving_BETWEEN_TUBES

class AnimationHumanManager(AnimationManager):
    def __init__(self):
        self._animation_state = "down"
        self._test_tube_source = None
        self._test_tube_destination = None

    def process_collision(self, test_tube):

        if self.animation_state == "down" and not test_tube.is_empty():
            self.animation_state = "moving_up"
            self.test_tube_source = test_tube
            self.test_tube_source.set_animation_up(self.handle_finish_animation_move_up)
            return None

        if self.animation_state == "up" and (test_tube is None or self.test_tube_source == test_tube):
            self.animation_state = "moving_down"
            self.test_tube_source.set_animation_down(self.handle_finish_animation_move_down)
            return None

        if self.animation_state == "up" and test_tube is not None and self.test_tube_source != test_tube:
            self.animation_state = "moving_between_tubes"
            return MoveForHuman(self.test_tube_source, test_tube)

    def animation_pending(self):
        return self.animation_state != "down" and self.animation_state != "up"

    # Animation Finisher Handlers
    def handle_finish_animation_move_up(self):
        self.animation_state = "up"

    def handle_finish_animation_move_down(self):
        self.animation_state = "down"
        self.test_tube_source = None

    def execute_move_animation(self, move):
        self.test_tube_destination = move.destination_test_tube
        self.test_tube_source.set_animation_between_tubes(self.test_tube_destination.rect,
                                                          self.handle_finish_animation_move_between_tubes)

    def reverse_move_animation(self):
        self.animation_state = "up"

    # Todo:Refactor
    def handle_finish_animation_move_between_tubes(self):

        ball_test = self.test_tube_source.balls.pop()
        array_aux = []

        for ball in self.test_tube_destination.balls:
            array_aux.append(ball.value)

        array_aux.append(ball_test.value)
        self.test_tube_destination.produce_ball(array_aux)

        self.animation_state = "down"
        self.test_tube_source = None
        self.test_tube_destination = None

    # Getters and Setters
    @property
    def animation_state(self):
        return self._animation_state

    @animation_state.setter
    def animation_state(self, value):
        self._animation_state = value

    @property
    def test_tube_source(self):
        return self._test_tube_source

    @test_tube_source.setter
    def test_tube_source(self, value):
        self._test_tube_source = value

    @property
    def test_tube_destination(self):
        return self._test_tube_destination

    @test_tube_destination.setter
    def test_tube_destination(self, value):
        self._test_tube_destination = value
