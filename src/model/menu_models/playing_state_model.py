import os

import pygame

from model.drawable import Drawable
from model.elements.test_tube import TestTube


class PlayingStateModel(Drawable):

    def __init__(self):
        self._background = pygame.image.load(os.path.join('../', 'assets', 'img', 'background.jpg'))
        self._test_tubes = [TestTube()]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        for test_tube in self.test_tubes:
            test_tube.draw(screen)

        pygame.display.update()

    @property
    def test_tubes(self):
        return self._test_tubes

    @property
    def background(self):
        return self._background
