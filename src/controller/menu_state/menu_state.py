class MenuState:
    def __init__(self, game):
        self._game = game

    def run(self):
        pass

    @property
    def game(self):
        return self._game
