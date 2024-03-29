import os

import pygame

from controller.events.event_manager_strategy.home_event_manager import HomeEventManager
from controller.menu_state.menu_state import MenuState
from controller.menu_state.states.choose_bot_state import ChooseBotState
from controller.menu_state.states.human_playing_state import HumanPlayingState
from model.elements.button import Button
from model.menu_models.home_state_model import HomeStateModel
from model.menu_models.playing_state_model import PlayingStateModel


class HomeState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)
        self._event_manager = HomeEventManager(model)

        button_play_human = Button(pygame.Rect(model.width // 2 - 400 // 2, 2 * model.height // 6, 400, 100),
                                   "Play as Human", self.change_to_state_human_playing)

        button_play_bot = Button(pygame.Rect(model.width // 2 - 400 // 2, 3 * model.height // 6, 400, 100),
                                 "Play as BOT", self.change_to_state_choose_bot)

        self.model.buttons.append(button_play_human)
        self.model.buttons.append(button_play_bot)
        self.running = True

        pygame.mixer.music.load(os.path.join('../', 'assets', 'sounds', 'music.wav'))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def run(self):

        while self.running:

            self.model.update()
            self.model.draw(self.game.view)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    break

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    button = self._event_manager.handle_mouse_event(event)
                    if button is not None:
                        self.running = False
                        return button.callback()

    def change_to_state_human_playing(self):
        self.game.menu_state = HumanPlayingState(self.game,
                                                 PlayingStateModel((self.game.view.width, self.game.view.height)))
        self.game.run()

    def change_to_state_choose_bot(self):
        self.game.menu_state = ChooseBotState(self.game, HomeStateModel((self.game.view.width, self.game.view.height)))
        self.game.run()
