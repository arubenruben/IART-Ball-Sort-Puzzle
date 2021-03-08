from game import Game
from src.model.menu_models.playing_state_model import PlayingStateModel
from src.view.view import View

if __name__ == '__main__':
    screen_width = 1024
    screen_height = 800
    fps = 60

    view = View((screen_width, screen_height), fps)
    model = PlayingStateModel((screen_width, screen_height))
    game = Game(model, view)
    game.run()
