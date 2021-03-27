from controller.menu_state.menu_state import MenuState
from controller.menu_state.states.defeat_state import DefeatState
from controller.menu_state.states.victory_state import VictoryState
from model.menu_models.home_state_model import HomeStateModel


class PlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game, model)

    def is_solved(self, test_tubes):
        for tube in test_tubes:
            if not tube.is_solved():
                return False
        return True

    def change_to_state_victory(self):
        self.game.menu_state = VictoryState(self.game, HomeStateModel((self.game.view.width, self.game.view.height)))
        return self.game.run()

    def change_to_state_defeat(self):
        self.game.menu_state = DefeatState(self.game, HomeStateModel((self.game.view.width, self.game.view.height)))
        return self.game.run()
