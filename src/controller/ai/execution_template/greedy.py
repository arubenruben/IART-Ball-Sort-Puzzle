from controller.menu_state.states.ai_playing_state import AIPlayingState
from model.headers.bot_searching_header import BotSearchingHeader


class Greedy(AIPlayingState):
    def __init__(self, game, model, heuristic):
        super().__init__(game, model)
        self._heuristic = heuristic
        self._staring_header = BotSearchingHeader("Greedy")
        self.model.header = self._staring_header

    def exec(self, child):
        child.h = self._heuristic.evaluate(child)
        self.queue.append(child)

    def extract(self):
        self.queue.sort(key=get_greedy_value, reverse=True)

        self.current_node = self.queue.pop()
        self.visited.append(self.current_node)

    def evaluate(self, child):
        return 0


def get_greedy_value(node):
    return node.h
