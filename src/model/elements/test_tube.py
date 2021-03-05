import os

import pygame

from src.model.drawable import Drawable
from src.model.elements.ball import Ball


class TestTube(Drawable):

    def __init__(self, balls, rect):
        self._background_image = pygame.image.load(os.path.join('../', 'assets', 'img', 'test_tube.png'))
        self._rect = rect
        self._balls = []

        for i in range(len(balls)):
            if balls[1] == 0:
                continue

            self._balls.append(Ball(balls[i], i, self.rect))

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
