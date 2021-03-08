import pygame

from src.model.drawable import Drawable
from src.model.utils.colors import color_converter


class Ball(Drawable):
    def __init__(self, value, center, radius):
        self._x_center, self._y_center = center
        self._radius = radius
        self._rect = pygame.Rect(self.x_center - self.radius, self.y_center + self.radius, 2 * radius, 2 * radius)
        self._value = value
        self._color = color_converter(self.value)

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_center, self.y_center), self.radius)

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

    @property
    def x_center(self):
        return self._x_center

    @property
    def y_center(self):
        return self._y_center

    @property
    def radius(self):
        return self._radius
