from src.controller.menu_state.states.ai_playing_state import AIPlayingState
from src.model.headers.bot_searching_header import BotSearchingHeader


class AStar(AIPlayingState):
    def __init__(self, game, model, heuristic):
        super().__init__(game, model)
        self._heuristic = heuristic
        self._staring_header = BotSearchingHeader("A STAR")
        self.model.header = self._staring_header

    def exec(self, child):
        child.h = self._heuristic.evaluate(child)

        if self.is_solved(child.state.test_tubes):
            child.g = 0
            child.h = 0

        self.queue.append(child)

    def extract(self):
        self.queue.sort(key=get_a_star_value, reverse=True)
        if len(self.queue) > 0:
            self.current_node = self.queue.pop()
            self.visited.append(self.current_node)


def get_a_star_value(node):
    return node.g + node.h
