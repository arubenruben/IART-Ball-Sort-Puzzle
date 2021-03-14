import os

import pygame

from src.model.drawable import Drawable
from src.model.utils.State import State
from src.model.utils.level_factory.level_creator import LevelCreator


class PlayingStateModel(Drawable):

    def __init__(self, screen_dimension):
        self.width, self.height = screen_dimension
        self._background = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'background.jpg')),
            (self.width, self.height))
        self._level_creator = LevelCreator()
        self._test_tubes = self._level_creator.create(1, (self.width, self.height))
        self._state = State(self._test_tubes)
        self._level = 1

    def update(self):
        for test_tube in self.state.test_tubes:
            test_tube.update()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        for test_tube in self.state.test_tubes:
            test_tube.draw(screen)

        pygame.display.update()

    @property
    def state(self):
        return self._state

    @property
    def background(self):
        return self._background

    def next_level(self):
        self._level += 1
        self._state = State(self._level_creator.create(self._level, (self.width, self.height)))

        return self.state

    @property
    def test_tubes(self):
        return self._test_tubes
