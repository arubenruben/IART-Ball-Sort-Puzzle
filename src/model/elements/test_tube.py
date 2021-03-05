import os

import pygame

from src.model.drawable import Drawable


class TestTube(Drawable):

    def __init__(self, balls, rect):
        self._background_image = pygame.image.load(os.path.join('../', 'assets', 'img', 'test_tube.png'))
        self._balls = balls
        self._rect = rect

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, self.rect)
        for ball in self.balls:
            pass
            # ball.draw(screen)

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
