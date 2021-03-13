import itertools
from copy import copy

from src.controller.move import Move

import pygame

from src.controller.menu_state.states.playing_state import PlayingState
from src.controller.menu_state.utils.utils import *


class AiPlayingState(PlayingState):
    def bfs(self):
        tubes = [copy(tube) for tube in self.model.test_tubes]

        # All possible permutations between tubes
        plays = list(itertools.permutations([n for n in range(len(tubes))], 2))

        start_node = Node([copy(tube) for tube in tubes], None, 0, None)
        visited = set([start_node])
        queue = [start_node]

        while queue:
            parent = queue.pop(0)
            if is_solved(parent.test_tubes):
                while 1:
                    if parent._depth == 0:
                        break
                    print(parent.operator._idx1, parent.operator._idx2)
                    parent = parent.parent

                return parent
            for play in plays:
                aux = [copy(tube) for tube in parent.test_tubes]
                curr_move = Move(aux[play[0]], aux[play[1]], play[0], play[1])
                if curr_move.move_ball():
                    child = Node(aux, parent, parent.depth + 1, curr_move)
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)

        return None
