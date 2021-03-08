import pygame


class View:
    def __init__(self, screen_dimension, fps):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.display.set_caption("Ball-Sort")

        self._width, self._height = screen_dimension
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._fps = fps

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def screen(self):
        return self._screen

    @property
    def clock(self):
        return self._clock

    @property
    def fps(self):
        return self._fps
