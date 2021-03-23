import pygame

from src.controller.events.event_manager_strategy.home_event_manager import HomeEventManager
from src.controller.menu_state.menu_state import MenuState
from src.model.headers.victory_header import VictoryHeader


class VictoryState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)
        self._event_manager = HomeEventManager(model)
        self.running = True
        self.model.header = VictoryHeader()

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
