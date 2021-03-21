from src.controller.AI.execution_template.bfs import BFS
from src.controller.AI.execution_template.dfs import DFS
from src.controller.menu_state.states.human_playing_state import HumanPlayingState


class Game:
    def __init__(self, model, view):
        self._view = view
        self._menu_state = HumanPlayingState(self, model)

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
