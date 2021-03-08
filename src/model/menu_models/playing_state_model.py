import os

import pygame

from src.model.drawable import Drawable
from src.model.utils.level_factory.level_creator import LevelCreator


class PlayingStateModel(Drawable):

    def __init__(self, screen_dimension):
        width, height = screen_dimension

        self._background = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'background.jpg')),
            (width, height))
        self._level_creator = LevelCreator()
        self._test_tubes = self._level_creator.create(1, (width, height))

    def update(self):
        for test_tube in self.test_tubes:
            test_tube.update()

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
