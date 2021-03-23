from src.controller.menu_state.states.ai_playing_state import AIPlayingState
from src.model.headers.bot_searching_header import BotSearchingHeader


class DFS(AIPlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)
        self._staring_header = BotSearchingHeader("DFS")
        self.model.header = self._staring_header

    def exec(self, child):
        self.queue.append(child)

    def extract(self):
        self.current_node = self.queue.pop()
        self.visited.append(self.current_node)
