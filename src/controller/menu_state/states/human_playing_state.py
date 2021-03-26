import os

import pygame

from src.controller.events.event_manager_strategy.human_playing_event_manager import HumanPlayingEventManager
from src.controller.menu_state.states.playing_state import PlayingState
from src.model.headers.human_playing_header import HumanPlayingHeader
from src.view.animation_managers.animation_human_manager import AnimationHumanManager
from src.controller.AI.execution_template.a_star import AStar
from src.controller.AI.heuristics.concrete_heuristics.entropy import EntropyHeuristic
from src.controller.AI.node import Node
from src.model.elements.button import Button


class HumanPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

        # Todo:Order Matters refactor
        self._animation_manager = AnimationHumanManager()
        self._event_manager = HumanPlayingEventManager(self._animation_manager, model)
        self.running = True
        self.model.header = HumanPlayingHeader()
        self.model.header.statistics.current_level = self.model.level
        button_level_reset = Button(pygame.Rect(model.width-150,0,150,50),"Reset Level",self.reset_level)
        self.model.buttons.append(button_level_reset)

    def run(self):
        while self.running:
            move = None

            self.game.view.clock.tick(self.game.view.fps)
            self.model.update()
            self.model.draw(self.game.view)

            if self.is_solved(self.model.state.test_tubes):
                if self.model.next_level():
                    self.reset()
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
                if(type(move).__name__=="Button"):
                    move.callback()
                    self.reset()
                elif move.validate():
                    move.execute(self._animation_manager)
                    self.model.header.statistics.plays_done += 1
                    print(self.get_hint().destination_index)
                    print()
                else:
                    move.fail(self._animation_manager)

    def get_hint(self):
        current_node = Node(self.model.state.clone(), None, 0, None)
        bot = AStar(self.game, self.model, EntropyHeuristic())
        move = bot.give_hint(current_node)
        return move

    def reset_level(self):
        self.model.reset_level()
        return

    def reset(self):
        self._animation_manager = AnimationHumanManager()
        self._event_manager = HumanPlayingEventManager(self._animation_manager, self.model)
        self.model.header = HumanPlayingHeader()
        self.model.header.statistics.current_level = self.model.level