from src.controller.menu_state.menu_state import MenuState


class PlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)
