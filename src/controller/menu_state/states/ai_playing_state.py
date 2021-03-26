import time
from copy import copy

import pygame

from src.controller.ai.move_generator import MoveGenerator
from src.controller.ai.node import Node
from src.controller.menu_state.states.playing_state import PlayingState
from src.model.headers.bot_simulating_header import BotSimulatingHeader
from src.model.move import Move
from src.view.animation_managers.animation_bot_manager import AnimationBotManager


class AIPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)
        self._move_generator = MoveGenerator(len(self.model.state.test_tubes))

        self._starting_state = self.model.state.clone()

        self._current_node = Node(self.model.state.clone(), None, 0, None)

        self._animation_manager = AnimationBotManager()

        self._queue = []

        self._visited = [self._current_node]

        self._staring_header = None

        self._running = True

    def run(self):

        solved = False

        while self._running:
            self.update_and_draw_state()

            if self.is_solved(self.current_node.state.test_tubes):
                solved = True
                break

            self.event_processing()

            self.node_expansion()

            self.extract()

            if len(self.queue) == 0:
                print("No possible moves")
                solved = False
                break

        if solved is False:
            return print("No solution")
        else:
            self.draw_solution()
            if self.model.next_level():
                self.reset()
                return self.run()
            else:
                self._running = False
                return self.change_to_state_victory()

    # Template Methods
    def exec(self, child):
        pass

    def extract(self):
        pass

    def event_processing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    def update_and_draw_state(self):
        self.model.update()
        self.model.draw(self.game.view)

    def node_expansion(self):
        for play in self._move_generator.plays:

            curr_move = Move(play[0], play[1])

            if curr_move.validate(self.current_node.state):

                state_clone = self.current_node.state.clone()

                curr_move.execute(state_clone)

                child = Node(state_clone, self.current_node.clone(), self.current_node.depth + 1,
                             copy(curr_move))

                unique = True

                for visited_node in self.visited:
                    if child == visited_node:
                        unique = False
                        break

                for node_in_queue in self.queue:
                    if child == node_in_queue:
                        unique = False
                        break

                if unique:
                    self.exec(child)
                    self.model.header.statistics.current_depth = child.depth
                    self.model.header.statistics.visited_queue_length = len(self.visited)
                    self.model.header.statistics.queue_length = len(self.queue)

    def draw_solution(self):

        self.model.header = BotSimulatingHeader()
        self.model.header.statistics.current_level = self.model.level

        path = []
        curr_node = self.visited[len(self.visited) - 1]
        while curr_node.parent is not None:
            path.append(curr_node)
            curr_node = curr_node.parent

        path.reverse()

        self.model.state = self._starting_state.clone()

        while len(path) > 0 or self._animation_manager.animation_pending:
            self.model.header.statistics.plays_missing = len(path)
            self.game.view.clock.tick(self.game.view.fps)

            if not self._animation_manager.animation_pending and len(path):
                self._animation_manager.execute_move_animation(path.pop(0), self.model)

            self.model.update()
            self.model.draw(self.game.view)

        self._animation_manager.animation_pending = False

    # Getters and Setters
    @property
    def queue(self):
        return self._queue

    @property
    def current_node(self):
        return self._current_node

    @current_node.setter
    def current_node(self, value):
        self._current_node = value

    @property
    def visited(self):
        return self._visited

    def reset(self):
        self._move_generator = MoveGenerator(len(self.model.state.test_tubes))

        self._starting_state = self.model.state.clone()

        self._current_node = Node(self.model.state.clone(), None, 0, None)

        self._animation_manager = AnimationBotManager()

        self._queue = []

        self._visited = [self._current_node]

        self.model.header = self._staring_header
        self.model.header.statistics._starting_time_stamp = time.time()

    def give_hint(self):
        self.node_expansion()
        self.extract()
        return self.current_node
