import pygame

from src.controller.menu_state.menu_state import MenuState
from src.model.menu_models.playing_state_model import PlayingStateModel


class PlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game)
        self._model = model

    #def moveBall(self, tube1, tube2):
     #   if isMovePossible(tube1, tube2):

    #def isMovePossible(self, tube1, tube2):

