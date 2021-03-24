import os

import pygame

from src.controller.events.event_manager_strategy.human_playing_event_manager import HumanPlayingEventManager
from src.controller.menu_state.states.playing_state import PlayingState
from src.model.headers.human_playing_header import HumanPlayingHeader
from src.view.animation_managers.animation_human_manager import AnimationHumanManager


class HumanPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

        # Todo:Order Matters refactor
        self._animation_manager = AnimationHumanManager()
        self._event_manager = HumanPlayingEventManager(self._animation_manager, model.state)
        self.running = True
        self.model.header = HumanPlayingHeader()
        self.model.header.statistics.current_level = self.model.level

    def run(self):

        while self.running:
            move = None

            self.game.view.clock.tick(self.game.view.fps)

            self.model.update()
            self.model.draw(self.game.view)

            if self.is_solved(self.model.state.test_tubes):
                if self.model.next_level():
                    self._animation_manager = AnimationHumanManager()
                    self._event_manager = HumanPlayingEventManager(self._animation_manager, self.model.state)
                    self.model.header = HumanPlayingHeader()
                    self.model.header.statistics.current_level = self.model.level
                else:
                    self.running = False
                    return self.change_to_state_victory()

            # TODO:Test if game is possible. Game end

            # TODO:Capability of providing hints | Add Hints used in the statistics object

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    move = self._event_manager.handle_mouse_event(event)

            if move is not None:
                if move.validate():
                    move.execute(self._animation_manager)
                    self.model.header.statistics.plays_done += 1
                else:
                    move.fail(self._animation_manager)
