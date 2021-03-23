from src.model.drawable import Drawable
from src.model.headers.statistics import Statistics


class BotSimulatingHeader(Drawable):
    def __init__(self):
        self._statistics = Statistics()

    def update(self):
        pass

    def draw(self, view):
        offset_between_lines = view.height // 40
        first_line = view.font_36.render("I'm Simulating my solution for level: " + str(self.statistics.current_level),
                                         True, (255, 255, 255))
        view.screen.blit(first_line, (view.width // 2 - first_line.get_width() // 2, offset_between_lines))

        second_line = view.font_36.render("Plays missing: " + str(self.statistics.plays_missing),
                                          True, (255, 255, 255))
        view.screen.blit(second_line, (
            view.width // 2 - second_line.get_width() // 2, first_line.get_height() + offset_between_lines * 2))

    @property
    def statistics(self):
        return self._statistics
