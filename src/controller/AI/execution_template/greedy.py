from src.controller.menu_state.states.AI_playing_state import AIPlayingState


class Greedy(AIPlayingState):
    def __init__(self, game, model, heuristic):
        super().__init__(game, model)
        self._heuristic = heuristic

    def exec(self, child):
        child.h = self.evaluate(child)
        self.queue.insert(0, child)

    def extract(self):
        self.queue.sort(key=get_greedy_value)

        self.current_node = self.queue.pop()
        self.visited.append(self.current_node)

    def evaluate(self, child):
        return 0


def get_greedy_value(node):
    return node.h
