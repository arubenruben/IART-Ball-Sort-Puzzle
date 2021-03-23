from src.controller.ai.execution_template.a_star import AStar
from src.controller.ai.execution_template.dfs import DFS
from src.controller.ai.heuristics.concrete_heuristics.entropy import EntropyHeuristic
from src.controller.menu_state.states.home_state import HomeState
from src.model.menu_models.home_state_model import HomeStateModel
from src.model.menu_models.playing_state_model import PlayingStateModel


class Game:
    def __init__(self, view):
        self._view = view
        # self._menu_state = DFS(self, PlayingStateModel((view.width, view.height)))

        self._menu_state = HomeState(self, HomeStateModel((view.width, view.height)))

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
