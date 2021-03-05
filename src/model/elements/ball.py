from model.drawable import Drawable


class Ball(Drawable):
    def __init__(self):
        self._color = None

    def update(self):
        pass

    def draw(self, screen):
        pass

    @property
    def color(self):
        return self._color
