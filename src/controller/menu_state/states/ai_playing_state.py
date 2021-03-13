import itertools
from copy import copy

from src.controller.menu_state.states.playing_state import PlayingState
from src.controller.menu_state.utils.utils import *


class AIPlayingState(PlayingState):
    def __init__(self, game, model):
        super().__init__(game, model)

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

            # Todo:Get the move
            move = None

            self.model.update()

            self.model.draw(self.game.view.screen)

            if move is None:
                continue

            if move.validate():
                move.execute(self.animation_manager)
            else:
                move.fail(self.animation_manager)

        pygame.quit()
