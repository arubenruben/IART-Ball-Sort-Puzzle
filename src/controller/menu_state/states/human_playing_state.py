import os
from copy import copy

import pygame

from src.controller.ai.execution_template.a_star import AStar
from src.controller.ai.heuristics.concrete_heuristics.distance import DistanceHeuristic
from src.controller.ai.node import Node
from src.controller.events.event_manager_strategy.human_playing_event_manager import HumanPlayingEventManager
from src.controller.menu_state.states.playing_state import PlayingState
from src.model.headers.human_playing_header import HumanPlayingHeader
from src.view.animation_managers.animation_human_manager import AnimationHumanManager


class HumanPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

        # Todo:Order Matters refactor
        self._animation_manager = AnimationHumanManager()
        self._event_manager = HumanPlayingEventManager(self._animation_manager, model)
        self.running = True
        self.model.header = HumanPlayingHeader()
        self.model.header.statistics.current_level = self.model.level
        self._last_move = None

    def run(self):
        while self.running:
            move = None

            self.game.view.clock.tick(self.game.view.fps)

            self.model.update()
            self.model.draw(self.game.view)

            if self._animation_manager.animation_pending:
                continue

            if self.is_solved(self.model.state.test_tubes):
                if self.model.next_level():
                    self.reset()
                else:
                    self.running = False
                    return self.change_to_state_victory()

            if self.is_game_impossible():
                return self.change_to_state_defeat()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    break

                if event.type == pygame.KEYUP:
                    if self._event_manager.handle_keyboard_event(event):
                        self.get_hint()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    move = self._event_manager.handle_mouse_event(event)

            if move is not None:
                if move.validate():
                    self._last_move = Node(self.model.state.clone(), None, None, None)
                    move.execute(self._animation_manager)
                    self.model.header.statistics.plays_done += 1
                    self.model.header.hint = None
                else:
                    move.fail(self._animation_manager)

    def get_hint(self):
        current_header = self.model.header

        bot = AStar(self.game, self.model, DistanceHeuristic())

        best_node_possible = bot.give_hint()

        if best_node_possible is None:
            return

        self.model.header = current_header
        self.model.header.hint = str(
            best_node_possible.operator._origin_index + 1) + " to: " + str(
            best_node_possible.operator._destination_index + 1)
        self.model.header.statistics.hints_used += 1

    def is_game_impossible(self):

        current_header = self.model.header

        bot = AStar(self.game, self.model, DistanceHeuristic())

        self.model.header = current_header

        if bot.give_hint() is None:
            return True

        if len(bot.queue) == 1 and self._last_move is not None and bot.give_hint() == self._last_move:
            return True

        return False
