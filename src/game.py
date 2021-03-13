from controller.menu_state.states.human_playing_state import HumanPlayingState
from src.controller.menu_state.states.ai_playing_state import AIPlayingState


class Game:

    def __init__(self, model, view):
        self._view = view
        self._menu_state = AIPlayingState(self, model)

    def run(self):
        self._menu_state.run()

    @property
    def menu_state(self):
        return self._menu_state

    @menu_state.setter
    def menu_state(self, value):
        self._menu_state = value

    @property
    def view(self):
        return self._view
