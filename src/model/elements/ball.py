import pygame

from src.model.drawable import Drawable
from src.model.utils.colors import color_converter


class Ball(Drawable):
    def __init__(self, value, index, test_tube_rect):
        self._rect = test_tube_rect
        self._value = value
        self._index = index
        self._color = color_converter(self.value)

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.rect[0], self.rect[1]), 10)

    @property
    def value(self):
        return self._value

    @property
    def color(self):
        return self._color

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value
