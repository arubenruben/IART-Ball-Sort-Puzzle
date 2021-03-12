import pygame


from controller.menu_state.states.ai_playing_state import AiPlayingState
from controller.menu_state.states.human_playing_state import HumanPlayingState
from model.menu_models.playing_state_model import PlayingStateModel


class Game:

    def __init__(self, screen_width=640, screen_height=480, fps=60):
        # Order Matters
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        pygame.display.set_caption("Ball-Sort")
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode((screen_width, screen_height))

        self._screen_width = screen_width
        self._screen_height = screen_height
        self._fps = fps

        # Must be the last thing to be created
        self._menu_state = AiPlayingState(self, PlayingStateModel((screen_width, screen_height)))

    def run(self):
        self._menu_state.bfs()

    @property
    def screen(self):
        return self._screen

    @property
    def clock(self):
        return self._clock

    @property
    def fps(self):
        return self._fps

    @property
    def screen_width(self):
        return self._screen_width

    @property
    def screen_height(self):
        return self._screen_height
