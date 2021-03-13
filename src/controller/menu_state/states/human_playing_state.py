import pygame

from src.controller.events.event_manager_strategy.event_manager import EventManager
from src.controller.menu_state.menu_state import MenuState


class HumanPlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model, EventManager(model.state, game.view.animation_manager))

    def run(self):

        run = True

        while run:
            self.game.view.clock.tick(self.game.view.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.event_manager.handle_mouse_event(event)

            self.model.update()

            self.model.draw(self.game.view.screen)

        pygame.quit()
