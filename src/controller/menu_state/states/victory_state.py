import os

import pygame

from src.controller.events.event_manager_strategy.home_event_manager import HomeEventManager
from src.controller.menu_state.menu_state import MenuState
from src.model.elements.button import Button
from src.model.headers.victory_header import VictoryHeader
from src.model.menu_models.home_state_model import HomeStateModel


class VictoryState(MenuState):

    def __init__(self, game, model):
        super().__init__(game, model)
        self._event_manager = HomeEventManager(model)
        self.model.header = VictoryHeader()

        back_button = Button(pygame.Rect(model.width // 2 - 400 // 2, model.height // 2, 400, 100),
                             "Back to Home", self.change_state_home)

        self.model.buttons.append(back_button)

        pygame.mixer.music.load(os.path.join('../', 'assets', 'sounds', 'end_music.wav'))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

        self.running = True

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

    def change_state_home(self):
        from src.controller.menu_state.states.home_state import HomeState
        self.game.menu_state = HomeState(self.game, HomeStateModel((self.game.view.width, self.game.view.height)))
        return self.game.run()
