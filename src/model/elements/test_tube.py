import os

import pygame

from src.controller.events.event import FINISH_ANIMATION_UP_EVENT
from src.model.drawable import Drawable
from src.model.elements.ball import Ball


class TestTube(Drawable):

    def __init__(self, balls, rect):

        self._rect = rect
        self._balls = []

        self._animating_up = False
        self._animating_down = False
        self._animating_move = False

        self._speed_animation_up = 3
        self._speed_animation_down = 3

        self._frame_counter = 0

        self._background_image = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'test_tube.png')),
            (rect.width, rect.height))

        # Todo:Improve this
        for i in range(len(balls)):
            if balls[i] == 0:
                break

            self.balls.append(
                Ball(balls[i], i,
                     pygame.Rect(self.rect.left + (self.rect.width // 2), self.rect.bottom - 20 * i, 10, 10))
            )

    def update(self):

        if len(self.balls) == 0:
            return

        last_ball = self.balls[len(self.balls) - 1]
        self.frame_counter += 1

        if self._animating_up:
            # Todo:Change Condition to stop animation to became dependent of position
            if self.frame_counter > 30:
                self._animating_up = False
                return

            last_ball.rect = last_ball.rect.move(0, -self.speed_animation_up)
        elif self._animating_down:
            # Todo:Change Condition to stop animation to became dependent of position
            if self.frame_counter > 30:
                self._animating_up = False
                return

            last_ball.rect = last_ball.rect.move(0, +self.speed_animation_down)
        else:
            self.frame_counter = 0

    def draw(self, screen):
        screen.blit(self.background_image, self.rect)
        for ball in self.balls:
            ball.draw(screen)

    @property
    def balls(self):
        return self._balls

    @property
    def background_image(self):
        return self._background_image

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    def animation_up(self):

        if len(self.balls) == 0:
            return
        self.frame_counter = 0
        self._animating_up = True

    def animation_down(self):

        if len(self.balls) == 0:
            return
        self.frame_counter = 0
        self._animating_down = True

    def animation_move(self, test_tube_destination):

        if len(self.balls) == 0:
            return
        self.frame_counter = 0
        self._animating_move = True

    @property
    def speed_animation_up(self):
        return self._speed_animation_up

    @property
    def speed_animation_down(self):
        return self._speed_animation_down

    @property
    def frame_counter(self):
        return self._frame_counter

    @frame_counter.setter
    def frame_counter(self, value):
        self._frame_counter = value
