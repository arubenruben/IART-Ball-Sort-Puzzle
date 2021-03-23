import os

import pygame

from src.model.drawable import Drawable
from src.model.state import State
from src.model.utils.level_factory.level_creator import LevelCreator


class PlayingStateModel(Drawable):

    def __init__(self, screen_dimension):
        self.width, self.height = screen_dimension
        self._background = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'background.jpg')),
            (self.width, self.height))

        self._level_creator = LevelCreator()
        self._state = State(self._level_creator.create(1, (self.width, self.height)))
        self._level = 1
        self._header = None

    def update(self):

        if self.header:
            self.header.update()

        for test_tube in self.state.test_tubes:
            test_tube.update()

    def draw(self, view):
        view.screen.blit(self.background, (0, 0))

        for test_tube in self.state.test_tubes:
            test_tube.draw(view)

        if self.header:
            self.header.draw(view)

        pygame.display.update()

    def next_level(self):
        self._level += 1
        self.state = State(self._level_creator.create(self._level, (self.width, self.height)))

        return len(self.state.test_tubes) > 0

    @property
    def background(self):
        return self._background

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def level(self):
        return self._level
