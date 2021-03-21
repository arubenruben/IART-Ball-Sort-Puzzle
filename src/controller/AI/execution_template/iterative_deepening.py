from src.controller.AI.execution_template.dfs import DFS
from src.controller.menu_state.states.AI_playing_state import AIPlayingState


class IterativeDeepening(AIPlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

    def exec(self, current_iteration=None):
        pass
