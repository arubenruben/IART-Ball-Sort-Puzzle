import pygame

from src.controller.menu_state.states.playing_state import PlayingState
from src.model.elements.button import Button


class HomeState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

        button_play_human = Button()

        self.model.buttons.append()

    def run(self):

        run = True

        while run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.model.update()
            self.model.draw(self.game.view)

        pygame.quit()
