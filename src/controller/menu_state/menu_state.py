from src.controller.events.event_manager_strategy.event_manager import EventManager


class MenuState:
    def __init__(self, game, model, event_manager):
        self._game = game
        self._model = model
        self._event_manager = event_manager

    def run(self):
        pass

    @property
    def game(self):
        return self._game

    @property
    def model(self):
        return self._model

    @property
    def event_manager(self):
        return self._event_manager
