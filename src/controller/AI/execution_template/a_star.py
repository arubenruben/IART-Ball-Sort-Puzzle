from src.controller.menu_state.states.AI_playing_state import AIPlayingState


class AStar(AIPlayingState):
    def __init__(self, game, model, heuristic):
        super().__init__(game, model)
        self._heuristic = heuristic

    def exec(self, child):
        child.h = 0
        self.queue.insert(0, child)

    def extract(self):
        self.queue.sort(key=get_a_star_value)

        self.current_node = self.queue.pop()
        self.visited.append(self.current_node)


def get_a_star_value(node):
    return node.g + node.h
