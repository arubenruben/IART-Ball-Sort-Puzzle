import os

import pygame

from src.model.drawable import Drawable
from src.model.elements.ball import Ball


class TestTube(Drawable):

    def __init__(self, raw_balls, rect):
        self._rect = rect
        self._balls = []

        self._background_image = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'test_tube.png')),
            (rect.width, rect.height))

        self.produce_ball(raw_balls)

    def update(self):
        pass

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
