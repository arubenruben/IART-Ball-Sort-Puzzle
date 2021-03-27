import pygame

from model.drawable import Drawable


class Button(Drawable):
    def __init__(self, rect, text, callback):
        self._rect = rect
        self._text = text
        self._callback = callback

    def update(self):
        super().update()

    def draw(self, view):
        pygame.draw.rect(view.screen, (85, 85, 85), self._rect)
        first_line = view.font_36.render(self.text, True, (255, 255, 255))
        view.screen.blit(first_line, (
            self._rect.center[0] - first_line.get_width() // 2, self._rect.center[1] - first_line.get_height() // 2))

    @property
    def rect(self):
        return self._rect

    @property
    def text(self):
        return self._text

    @property
    def callback(self):
        return self._callback
