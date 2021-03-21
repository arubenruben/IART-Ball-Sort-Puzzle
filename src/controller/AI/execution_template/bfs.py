from src.controller.menu_state.states.AI_playing_state import AIPlayingState


class BFS(AIPlayingState):

    def __init__(self, game, model):
        super().__init__(game, model)

    def exec(self, child):
        self.queue.append(child)

    def extract(self):
        self.current_node = self.queue.pop()
        self.visited.append(self.current_node)
