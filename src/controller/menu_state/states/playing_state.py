from src.controller.menu_state.menu_state import MenuState


class PlayingState(MenuState):
    def __init__(self, game):
        super().__init__(game)

    def run(self):
        while True:
            self.game.clock.tick(self.game.fps)
