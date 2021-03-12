import pygame

from src.controller.menu_state.states.playing_state import PlayingState
from src.controller.menu_state.utils.utils import *


class AiPlayingState(PlayingState):
    def bfs(self):
        move_ball(self.model.test_tubes[0], self.model.test_tubes[-1])
        start_node = Node(self.model.test_tubes, None, 0, None)
        print(self.model.test_tubes[0].balls)
        # Not sure if list is best to save visited nodes
        visited = set([start_node])
        queue = [start_node]

        while queue:
            queue.pop(0)

