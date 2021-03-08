from src.controller.events.event_manager_strategy.event_manager import EventManager


class EventManagerPlayStateHuman(EventManager):
    def __init__(self, model):
        super().__init__(model)
        self._animation_type = "down"
        self._test_tube_animation_source = None
        self._test_tube_animation_destination = None

    def handle_mouse_event(self, pos):

        if self.animation_type == "moving":
            return

        test_tube_that_collide = None

        for test_tube in self.model.test_tubes:
            if test_tube.rect.collidepoint(pos):
                test_tube_that_collide = test_tube
                break

        if self.animation_type == "down":
            if test_tube_that_collide is None:
                return
            else:
                self.test_tube_animation_source = test_tube_that_collide
                test_tube_that_collide.animate_up(self.handle_move_up)

        elif self.animation_type == "up":
            if test_tube_that_collide is None or test_tube_that_collide == self.test_tube_animation_source:
                self.test_tube_animation_source.animate_down(self.handle_move_down)
            else:
                self.test_tube_animation_destination = test_tube_that_collide
                self.test_tube_animation_source.move_between_tubes(self.test_tube_animation_destination.rect,
                                                                   self.handle_moving_between_tubes)
        self.animation_type = "moving"

    def handle_move_up(self):
        self.animation_type = "up"

    def handle_move_down(self):
        self.test_tube_animation_source = None
        self.animation_type = "down"

    # TODO:Need to exchange the balls from one tube to another
    def handle_moving_between_tubes(self):
        self.test_tube_animation_source = None
        self.test_tube_animation_destination = None
        self.animation_type = "down"

    @property
    def animation_type(self):
        return self._animation_type

    @animation_type.setter
    def animation_type(self, value):
        self._animation_type = value

    @property
    def test_tube_animation_source(self):
        return self._test_tube_animation_source

    @test_tube_animation_source.setter
    def test_tube_animation_source(self, value):
        self._test_tube_animation_source = value

    @property
    def test_tube_animation_destination(self):
        return self._test_tube_animation_destination

    @test_tube_animation_destination.setter
    def test_tube_animation_destination(self, value):
        self._test_tube_animation_destination = value
