import pygame

from src.controller.menu_state.states.playing_state import PlayingState
from src.model.menu_models.playing_state_model import PlayingStateModel


class HumanPlayingState(PlayingState):

    def run(self):
        run = True

        while run:
            self.game.clock.tick(self.game.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_event(event)

            self.model.update()

            self.model.draw(self.game.screen)

        pygame.quit()

    def handle_mouse_event(self, event):
        print(event)

    @property
    def model(self):
        return self._model
