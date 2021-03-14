from src.controller.menu_state.states.AI_playing_state import AIPlayingState


class BFSAI(AIPlayingState):
    def exec(self, state_expansion):
        pass

    def evaluate(self, node_list):
        for node in node_list:
            node.cost = 1

    def print_state(self, state):
        for test_tube in state.test_tubes:
            print(test_tube.raw_ball_list())
        print("---------------------------")
