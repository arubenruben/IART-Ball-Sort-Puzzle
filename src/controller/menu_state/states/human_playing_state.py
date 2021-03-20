import pygame

from src.controller.events.event_manager_strategy.event_manager import EventManager
from src.controller.menu_state.menu_state import MenuState
from src.controller.utils.utils import is_solved
from src.view.animation_managers.animation_human_manager import AnimationHumanManager


class HumanPlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)

        # Todo:Order Matters refactor
        self._animation_manager = AnimationHumanManager()
        self._event_manager = EventManager(self._animation_manager, model.test_tubes)

    def run(self):

        run = True

        while run:
            move = None

            self.game.view.clock.tick(self.game.view.fps)

            if is_solved(self.model.test_tubes):
                if self.model.next_level() is None:
                    break
                else:
                    self._animation_manager = AnimationHumanManager()

            # TODO:Test if game is possible. Game end

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    move = self._event_manager.handle_mouse_event(event)

            self.model.update()
            self.model.draw(self.game.view.screen)

            if move is not None:
                if move.validate():
                    move.execute(self._animation_manager)
                else:
                    move.fail(self._animation_manager)

        pygame.quit()
