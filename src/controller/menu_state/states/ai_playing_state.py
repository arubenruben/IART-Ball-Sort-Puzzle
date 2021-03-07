import pygame

from src.controller.menu_state.states.playing_state import PlayingState


class AiPlayingState(PlayingState):
    def bfs(self):
        print(self._model._test_tubes[0]._balls[-1].color)
