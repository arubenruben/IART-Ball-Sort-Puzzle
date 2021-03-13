class MenuState:
    def __init__(self, game, model):
        self._game = game
        self._model = model

    def run(self):
        pass

    @property
    def game(self):
        return self._game

    @property
    def model(self):
        return self._model
