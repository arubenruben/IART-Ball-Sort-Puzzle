import pygame

from src.model.drawable import Drawable
from src.model.utils.colors import color_converter


class Ball(Drawable):
    def __init__(self, test_tube_rect, value, position_in_tube):
        self._position_in_tube = position_in_tube
        self._radius = test_tube_rect.width // 4
        self._correction_y = test_tube_rect.height // 8

        self._distance_between_ball = (test_tube_rect.height - (2 * self._correction_y + 8 * self._radius)) // 3

        self._x_center = test_tube_rect.center[0]
        self._y_center = test_tube_rect.bottom - 2 * self._radius * self._position_in_tube - self._correction_y - (
                self._distance_between_ball * self._position_in_tube)

        self._rect = pygame.Rect(
            self.x_center - self.radius, self.y_center - self.radius, 2 * self._radius, 2 * self._radius
        )
        self._value = value
        self._color = color_converter(self.value)

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.rect.centerx, self.rect.centery), self.radius)

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

    def __eq__(self, other):
        return self.value == other.value
