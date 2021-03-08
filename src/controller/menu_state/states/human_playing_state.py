import pygame

from src.controller.menu_state.menu_state import MenuState


class HumanPlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)

    def run(self):

        run = True

        while run:
            self.game.view.clock.tick(self.game.view.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_event(pygame.mouse.get_pos())

            self.model.update()

            self.model.draw(self.game.view.screen)

        pygame.quit()
