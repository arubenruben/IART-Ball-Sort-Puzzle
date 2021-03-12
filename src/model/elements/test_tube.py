import copy
import os

import pygame

from src.model.drawable import Drawable
from src.model.elements.ball import Ball


class TestTube(Drawable):

    def __init__(self, balls, rect):
        # Todo:Missing here a scale in the picture in order to dimensions work properly
        self._background_image = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'test_tube.png')),
            (rect.width, rect.height))
        self._rect = rect
        self._balls = []

        for i in range(len(balls)):
            if balls[i] == 0:
                break

            self.balls.append(
                Ball(balls[i], i,
                     pygame.Rect(self.rect.left + (self.rect.width // 2), self.rect.bottom - 20 * i, 10, 10))
            )

    def update(self):
        pass

    def __copy__(self):
        copy_obj = TestTube(self.balls, self.rect)
        for name, attr in self.__dict__.items():
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                copy_obj.__dict__[name] = attr.copy()
            else:
                copy_obj.__dict__[name] = copy.deepcopy(attr)
        return copy_obj

    def draw(self, screen):
        screen.blit(self.background_image, self.rect)
        for ball in self.balls:
            ball.draw(screen)

    def getFirstBall(self):
        if len(self._balls) > 0:
            return self._balls[len(self._balls)-1]
        return None 

    def isFull(self):
        return len(self._balls) == 4

    def isEmpty(self):
        return len(self._balls) == 0

    @property
    def balls(self):
        return self._balls

    @property
    def background_image(self):
        return self._background_image

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value
