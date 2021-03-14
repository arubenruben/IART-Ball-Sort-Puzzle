from src.controller.menu_state.states.AI_playing_state import AIPlayingState


class BFSAI(AIPlayingState):
    def exec(self, child):
        self.queue.append(child)

    def evaluate(self, node_list):
        for node in node_list:
            node.cost = 1
