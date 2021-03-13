# States: Down. Up. Moving_UP. Moving_DOWN Moving_BETWEEN_TUBES

class AnimationManager:
    def __init__(self):
        self._state = "down"
        self._test_tube_source = None
        self._test_tube_destination = None

    def process_collision(self, test_tube):

        if self.state == "down" and test_tube is not None and not test_tube.is_empty():
            self.state = "moving_up"
            self.test_tube_source = test_tube
            self.test_tube_source.set_animation_up(self.handle_finish_animation_move_up)

        elif self.state == "up" and (test_tube is None or self.test_tube_source == test_tube):
            self.state = "moving_down"
            self.test_tube_source.set_animation_down(self.handle_finish_animation_move_down)

        elif self.state == "up" and test_tube is not None and self.test_tube_source != test_tube and not test_tube.is_full():
            self.state = "moving_between_tubes"
            self._test_tube_destination = test_tube
            self.test_tube_source.set_animation_between_tubes(test_tube.rect,
                                                              self.handle_finish_animation_move_between_tubes)
        # Animation Finisher Handlers

    def handle_finish_animation_move_up(self):
        self.state = "up"

    def handle_finish_animation_move_down(self):
        self.state = "down"
        self.test_tube_source = None

    # Todo:Refactor
    def handle_finish_animation_move_between_tubes(self):

        ball_test = self.test_tube_source.balls.pop()
        array_aux = []

        for ball in self.test_tube_destination.balls:
            array_aux.append(ball.value)

        array_aux.append(ball_test.value)
        self.test_tube_destination.produce_ball(array_aux)

        self.state = "down"
        self.test_tube_source = None

        self.test_tube_destination = None

    # Getters and Setters

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def animation_pending(self):
        return self.state != "down" and self.state != "up"

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
