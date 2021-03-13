import pygame

from src.controller.AI.utils import is_solved
from src.controller.events.event_manager_strategy.event_manager import EventManager
from src.controller.menu_state.menu_state import MenuState
from src.view.animation_managers.animation_human_manager import AnimationHumanManager


class HumanPlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)

        # Todo:Order Matters refactor
        self._animationManager = AnimationHumanManager()
        self._event_manager = EventManager(self._animationManager)

    def run(self):
        run = True
        while run:
            move = None

            self.game.view.clock.tick(self.game.view.fps)

            if is_solved(self.model.state):
                if self.model.next_level() is None:
                    break
                else:
                    self.animation_manager.reset()

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
                move.execute(self.animation_manager)
            else:
                move.fail(self.animation_manager)

        pygame.quit()

    @property
    def event_manager(self):
        return self._event_manager

    @property
    def animation_manager(self):
        return self._animationManager
