import pygame

from src.controller.events.event_manager_strategy.strategies.event_manager_play_state_human import \
    EventManagerPlayStateHuman
from src.controller.menu_state.menu_state import MenuState


class HumanPlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)
        self._event_manager = EventManagerPlayStateHuman(model)

    def run(self):

        run = True

        while run:
            self.game.view.clock.tick(self.game.view.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.event_manager.handle_mouse_event(pygame.mouse.get_pos())

            self.model.update()
            self.model.draw(self.game.view.screen)

        pygame.quit()

    @property
    def event_manager(self):
        return self._event_manager
