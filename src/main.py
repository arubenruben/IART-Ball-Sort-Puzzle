from game import Game
from src.view.view import View

if __name__ == '__main__':
    screen_width = 1024
    screen_height = 800
    fps = 60

    view = View((screen_width, screen_height), fps)
    game = Game(view)
    game.run()
