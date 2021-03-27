import os

import pygame

from model.move_for_human import MoveForHuman
from view.animation_managers.animation_bot_manager import AnimationManager


# States: Down. Up. Moving_UP. Moving_DOWN Moving_BETWEEN_TUBES

class AnimationHumanManager(AnimationManager):
    def __init__(self):
        self._state = "down"
        self._test_tube_source = None
        self._test_tube_destination = None

    def process_collision(self, test_tube):

        if self.state == "down" and test_tube is not None and not test_tube.is_empty() and test_tube.is_solved() is not True:
            pygame.mixer.music.load(os.path.join('assets', 'sounds', 'push.wav'))
            pygame.mixer.music.play()

            self.state = "moving_up"
            self.test_tube_source = test_tube
            self.test_tube_source.set_animation_up(self.handle_finish_animation_move_up)
            return None

        if self.state == "up" and (test_tube is None or self.test_tube_source is test_tube):
            pygame.mixer.music.load(os.path.join('assets', 'sounds', 'move_fail.wav'))
            pygame.mixer.music.play()

            self.state = "moving_down"
            self.test_tube_source.set_animation_down(self.handle_finish_animation_move_down)
            return None

        if self.state == "up" and test_tube is not None and self.test_tube_source is not test_tube:
            self.state = "moving_between_tubes"
            return MoveForHuman(self.test_tube_source, test_tube)

    # Animation Finisher Handlers

    def handle_finish_animation_move_up(self):
        self.state = "up"

    def handle_finish_animation_move_down(self):
        self.state = "down"
        self.test_tube_source = None

    def execute_move_animation(self, move):
        self.test_tube_source = move.origin_test_tube
        self.test_tube_destination = move.destination_test_tube
        self.test_tube_source.set_animation_between_tubes(self.test_tube_destination.rect,
                                                          self.handle_finish_animation_move_between_tubes)

    def reverse_move_animation(self):
        self.state = "up"

    def reset(self):
        self.state = "down"
        self.test_tube_source = None
        self.test_tube_destination = None

    def handle_finish_animation_move_between_tubes(self):

        pygame.mixer.music.load(os.path.join('assets', 'sounds', 'pop.wav'))
        pygame.mixer.music.play()
        ball_test = self.test_tube_source.pop_ball()
        self.test_tube_destination.insert_ball(ball_test)
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
