from src.controller.menu_state.states.AI_playing_state import AIPlayingState
from src.model.headers.bot_searching_header import BotSearchingHeader


class BFS(AIPlayingState):

    def __init__(self, game, model):
        super().__init__(game, model)
        self.model.header = BotSearchingHeader("BFS")

    def exec(self, child):
        self.queue.append(child)

    def extract(self):
        self.current_node = self.queue.pop()
        self.visited.append(self.current_node)
