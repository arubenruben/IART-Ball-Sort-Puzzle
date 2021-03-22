import pygame

from src.controller.events.event_manager_strategy.event_manager import EventManager
from src.controller.menu_state.states.playing_state import PlayingState
from src.view.animation_managers.animation_human_manager import AnimationHumanManager


class HumanPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

        # Todo:Order Matters refactor
        self._animation_manager = AnimationHumanManager()
        self._event_manager = EventManager(self._animation_manager, model.state)

    def run(self):

        run = True
        while run:
            move = None

            self.game.view.clock.tick(self.game.view.fps)

            if self.is_solved(self.model.state.test_tubes):
                if self.model.next_level():
                    self._animation_manager = AnimationHumanManager()
                    self._event_manager = EventManager(self._animation_manager, self.model.state)
                else:
                    break

            # TODO:Test if game is possible. Game end

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    move = self._event_manager.handle_mouse_event(event)

            self.model.update()
            self.model.draw(self.game.view)

            if move is not None:
                if move.validate():
                    move.execute(self._animation_manager)
                else:
                    move.fail(self._animation_manager)

        pygame.quit()
