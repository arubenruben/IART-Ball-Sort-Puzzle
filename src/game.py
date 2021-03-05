import pygame

from controller.menu_state.states.human_playing_state import HumanPlayingState


class Game:
    def __init__(self, width=640, height=480, fps=60):
        self._menu_state = HumanPlayingState(self)

        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        pygame.display.set_caption("Ball-Sort")
        self._screen = pygame.display.set_mode((width, height))
        self._clock = pygame.time.Clock()
        self._fps = fps

    def run(self):
        self._menu_state.run()

    @property
    def screen(self):
        return self._screen

    @property
    def clock(self):
        return self._clock

    @property
    def fps(self):
        return self._fps
