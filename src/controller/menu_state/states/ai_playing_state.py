import itertools
from copy import copy

from src.controller.move import Move

import pygame

from src.controller.menu_state.states.playing_state import PlayingState
from src.controller.menu_state.utils.utils import *


class AiPlayingState(PlayingState):
    def bfs(self):
        tubes = [copy(tube) for tube in self.model.state]

        # All possible permutations between tubes
        plays = list(itertools.permutations([n for n in range(len(tubes))], 2))

        start_node = Node([copy(tube) for tube in tubes], None, 0, None)
        visited = set([start_node])
        queue = list()
        queue.append(start_node)

        while queue:
            parent = queue.pop(0)
            if is_solved(parent.test_tubes):
                while 1:
                    if parent.depth == 0:
                        break
                    print(parent.operator.tube1idx, parent.operator.tube2idx)
                    parent = parent.parent

                return parent
            for play in plays:
                curr_move = Move(play[0], play[1])
                if is_move_possible(parent.test_tubes[play[0]], parent.test_tubes[play[1]]):
                    aux = [copy(tube) for tube in parent.test_tubes]
                    move_ball(aux[play[0]], aux[play[1]])
                    child = Node(aux, parent, parent.depth + 1, curr_move)
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)

        return None
