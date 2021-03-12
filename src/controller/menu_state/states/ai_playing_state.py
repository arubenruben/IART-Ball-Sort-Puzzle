from copy import deepcopy

import pygame

from src.controller.menu_state.states.playing_state import PlayingState
from src.controller.menu_state.utils.utils import *


class AiPlayingState(PlayingState):
    def bfs(self):
        # All possible permutations between tubes
        plays_indexes = list(itertools.permutations([n for n in range(7)], 2))
        tubes = [copy(tube) for tube in self.model.test_tubes]
        start_node = Node(self.model.test_tubes, None, 0, None)
        print(self.model.test_tubes[-1])
        # Not sure if list is best to save visited nodes
        visited = set([start_node])
        queue = [start_node]

        while queue:
            queue.pop(0)

