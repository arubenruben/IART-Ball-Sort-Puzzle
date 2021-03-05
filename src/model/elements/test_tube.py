import os

import pygame

from src.model.drawable import Drawable


class TestTube(Drawable):

    def __init__(self):
        self._balls = []
        self._background_image = pygame.image.load(os.path.join('../', 'assets', 'img', 'test_tube.png'))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background_image, (0, 0))
        for ball in self.balls:
            ball.draw(screen)

    @property
    def balls(self):
        return self._balls

    @property
    def background_image(self):
        return self._background_image
