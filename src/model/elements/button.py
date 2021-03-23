from src.model.drawable import Drawable


class Button(Drawable):
    def __init__(self, rect, text):
        self._rect = rect
        self._text = text

    def update(self):
        super().update()

    def draw(self, view):
        super().draw(view)

    @property
    def rect(self):
        return self._rect

    @property
    def text(self):
        return self._text
