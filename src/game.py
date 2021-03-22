from src.controller.AI.execution_template.a_star import AStar
from src.controller.AI.execution_template.dfs import DFS
from src.controller.AI.execution_template.greedy import Greedy
from src.controller.AI.heuristics.concrete_heuristics.entropy import EntropyHeuristic


class Game:
    def __init__(self, model, view):
        self._view = view
        self._menu_state = DFS(self, model)

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
