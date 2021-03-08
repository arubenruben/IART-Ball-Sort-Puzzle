import os

import pygame

from src.model.drawable import Drawable
from src.model.elements.ball import Ball


class TestTube(Drawable):

    def __init__(self, raw_balls, rect):
        self._rect = rect
        self._balls = []
        self._animating_up = False
        self._animating_down = False
        self._animating_move = False
        self._speed_y = 10
        self._speed_x = 10
        self._callback = None
        self._destination_rect = None

        self._background_image = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'test_tube.png')),
            (rect.width, rect.height))

        self.produce_ball(raw_balls)

    def update(self):
        if self.animating_up:
            return self.animate_up()
        if self.animating_down:
            return self.animate_down()
        if self.animating_move:
            return self.move_between_tubes()

    def draw(self, screen):
        screen.blit(self.background_image, self.rect)
        for ball in self.balls:
            ball.draw(screen)

    def produce_ball(self, raw_balls):
        ball_radius = self.rect.width // 4
        correction_y = self.rect.height // 8
        distance_between_ball = 3

        for i in range(len(raw_balls)):
            if raw_balls[i] == 0:
                return
            self.balls.append(
                Ball(
                    raw_balls[i],
                    (
                        self.rect.center[0],
                        self.rect.bottom - 2 * ball_radius * i - correction_y - (distance_between_ball * i)
                    ),
                    ball_radius
                )
            )

    def animate_up(self, callback=None):
        if callback is not None:
            self.callback = callback
            return

    def animate_down(self, callback=None):
        if callback is not None:
            self.callback = callback
            return

    def move_between_tubes(self, destination_rect=None, callback=None):
        if destination_rect is not None and callback is not None:
            self.destination_rect = destination_rect
            self.callback = callback
            return

    # Getter and Setters
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

    @property
    def speed_x(self):
        return self._speed_x

    @property
    def speed_y(self):
        return self._speed_y

    @property
    def animating_up(self):
        return self._animating_up

    @property
    def animating_down(self):
        return self._animating_down

    @property
    def animating_move(self):
        return self._animating_move

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value):
        self._callback = value

    @property
    def destination_rect(self):
        return self._destination_rect

    @destination_rect.setter
    def destination_rect(self, value):
        self._destination_rect = value
