from src.controller.menu_state.menu_state import MenuState


class PlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)

    def is_solved(self, test_tubes):
        for tube in test_tubes:
            if not tube.is_solved():
                return False
        return True

    def change_to_state_victory(self):
        pass

    def change_to_state_defeat(self):
        pass
