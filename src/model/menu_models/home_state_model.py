import os

import pygame

from src.model.drawable import Drawable
from src.model.headers.home_header import HomeHeader


class HomeStateModel(Drawable):
    def __init__(self, screen_dimension):
        self.width, self.height = screen_dimension
        self._background = pygame.transform.scale(
            pygame.image.load(os.path.join('./', 'assets', 'img', 'background.jpg')),
            (self.width, self.height))

        self._header = HomeHeader()
        self._buttons = []
        pygame.mixer.music.load(os.path.join('../', 'assets', 'sounds', 'music.wav'))
        pygame.mixer.music.play(-1)

    def update(self):
        super().update()

    def draw(self, view):
        view.screen.blit(self.background, (0, 0))

        self.header.draw(view)

        for button in self.buttons:
            button.draw(view)

        pygame.display.update()

    @property
    def background(self):
        return self._background

    @property
    def buttons(self):
        return self._buttons

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value
