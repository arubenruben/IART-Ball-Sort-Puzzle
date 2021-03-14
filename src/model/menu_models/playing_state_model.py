import os

import pygame

from src.model.drawable import Drawable
from src.model.utils.level_factory.level_creator import LevelCreator


class PlayingStateModel(Drawable):

    def __init__(self, screen_dimension):
        self.width, self.height = screen_dimension
        self._background = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'background.jpg')),
            (self.width, self.height))
        self._level_creator = LevelCreator()

        self._test_tubes = self._level_creator.create(1, (self.width, self.height))
        self._level = 1

    def update(self):
        for test_tube in self.test_tubes:
            test_tube.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        for test_tube in self.test_tubes:
            test_tube.draw(screen)

        pygame.display.update()

    @property
    def background(self):
        return self._background

    def next_level(self):
        self._level += 1
        self.test_tubes = self._level_creator.create(self._level, (self.width, self.height))

        return self.test_tubes

    @property
    def test_tubes(self):
        return self._test_tubes

    @test_tubes.setter
    def test_tubes(self, value):
        self._test_tubes = value
