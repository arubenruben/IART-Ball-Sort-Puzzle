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
        self._speed_y = 5
        self._speed_x = 5
        self._callback = None
        self._destination_rect = None
        self._original_ball_position = None
        self.distance_between_ball = 3
        self.ball_radius = self.rect.width // 4
        self.correction_y = self.rect.height // 8

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
        # TODO:DANGER DANGER DANGER DANGER REMOVER ISTO
        self._balls = []
        # DANGER DANGER DANGER DANGER
        for i in range(len(raw_balls)):
            if raw_balls[i] == 0:
                return
            self.balls.append(
                Ball(
                    raw_balls[i],
                    (
                        self.rect.center[0],
                        self.rect.bottom - 2 * self.ball_radius * i - self.correction_y - (
                                self.distance_between_ball * i)
                    ),
                    self.ball_radius
                )
            )

    def animate_up(self, callback=None):
        # TODO:Refactor this if
        if len(self.balls) == 0:
            return

        ball = self.balls[(len(self.balls) - 1)]

        if callback is not None:
            self.callback = callback
            self.animating_up = True
            self.original_ball_position = ball.rect.copy()
            return

        if ball.rect.top <= self.rect.top - self.rect.height // 4:
            self.callback()
            self.reset_animations()
        else:
            ball.rect = ball.rect.move(0, -self.speed_y)

    def animate_down(self, callback=None):
        if callback is not None:
            self.callback = callback
            self.animating_down = True
            return

        ball = self.balls[(len(self.balls) - 1)]

        if ball.rect.top >= self.original_ball_position.bottom - 8 * self.speed_y:
            ball.rect = self.original_ball_position.copy()
            self.callback()
            self.reset_animations()
        else:
            ball.rect = ball.rect.move(0, self.speed_y)

    def move_between_tubes(self, destination_rect=None, callback=None):
        if destination_rect is not None and callback is not None:
            self.destination_rect = destination_rect
            self.callback = callback
            self.animating_move = True
            return

        ball = self.balls[(len(self.balls) - 1)]
        # Todo:Move Animation
        if True:
            self.callback()
            self.reset_animations()
            # else:
            #   ball.rect = ball.rect.move(0, self.speed_y)

    def reset_animations(self):
        self.callback = None
        self.animating_up = False
        self.animating_down = False
        self.animating_move = False

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

    @animating_up.setter
    def animating_up(self, value):
        self._animating_up = value

    @property
    def animating_down(self):
        return self._animating_down

    @animating_down.setter
    def animating_down(self, value):
        self._animating_down = value

    @property
    def animating_move(self):
        return self._animating_move

    @animating_move.setter
    def animating_move(self, value):
        self._animating_move = value

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

    @property
    def original_ball_position(self):
        return self._original_ball_position

    @original_ball_position.setter
    def original_ball_position(self, value):
        self._original_ball_position = value
