import pygame

from src.controller.events.event_manager_strategy.event_manager import EventManager
from src.controller.menu_state.menu_state import MenuState


class HumanPlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model, EventManager(model.state, game.view.animation_manager))

    def run(self):
        run = True

        while run:
            move = None

            self.game.view.clock.tick(self.game.view.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    move = self.event_manager.handle_mouse_event(event)

            self.model.update()

            self.model.draw(self.game.view.screen)

            if move is None:
                continue

            new_state = None

            if move.validate(self.model.state):
                new_state = move.execute(self.model.state, self.game.view.animation_manager)

            if new_state is not None:
                pass

        pygame.quit()
