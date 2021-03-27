from controller.menu_state.states.home_state import HomeState
from model.menu_models.home_state_model import HomeStateModel


class Game:
    def __init__(self, view):
        self._view = view

        self._menu_state = HomeState(self, HomeStateModel((view.width, view.height)))

    def run(self):
        self._menu_state.run()

    @property
    def menu_state(self):
        return self._menu_state

    @menu_state.setter
    def menu_state(self, value):
        self._menu_state = value

    @property
    def view(self):
        return self._view
