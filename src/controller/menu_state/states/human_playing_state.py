import pygame

from src.controller.events.event_manager_strategy.event_manager import EventManager
from src.controller.menu_state.menu_state import MenuState
from src.controller.menu_state.utils.utils import is_solved


class HumanPlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model, EventManager(game.view.animation_manager))

    def run(self):
        run = True

        while run:
            move = None

            self.game.view.clock.tick(self.game.view.fps)

            if is_solved(self.model.state):
                if self.model.next_level() is None:
                    break
                else:
                    self.game.view.animation_manager.reset()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    move = self.event_manager.handle_mouse_event(self.model.state, event)

            self.model.update()

            self.model.draw(self.game.view.screen)

            if move is None:
                continue

            if move.validate():
                move.execute(self.game.view.animation_manager)
            else:
                move.fail(self.game.view.animation_manager)

        pygame.quit()
