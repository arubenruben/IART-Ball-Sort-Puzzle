import pygame

from src.controller.menu_state.states.playing_state import PlayingState
from src.controller.menu_state.utils.utils import *


class AiPlayingState(PlayingState):
    def bfs(self):
        tubes = get_simplified_state(self.model.test_tubes)
        start_node = Node(tubes, None, 0, None)
        # Not sure if list is best to save visited nodes
        visited = [start_node]
        queue = [start_node]

        while queue:
            queue.pop(0)
