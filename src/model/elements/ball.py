import pygame

from model.drawable import Drawable
from model.utils.colors import color_converter


class Ball(Drawable):
    def __init__(self, value, index, rect):
        self._rect = rect
        self._value = value
        self._index = index
        self._color = color_converter(self.value)

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.rect.x, self.rect.y - 10-5), 10)

    def __eq__(self, other):
        return self.color == other.color

    def __hash__(self):
        return hash(tuple(self.color))

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
