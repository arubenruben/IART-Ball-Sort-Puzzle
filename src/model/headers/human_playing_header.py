import time

from src.model.drawable import Drawable
from src.model.headers.statistics import Statistics


class HumanPlayingHeader(Drawable):
    def __init__(self):
        self._statistics = Statistics()

    def update(self):
        self.statistics.current_time_stamp = time.time()

    def draw(self, view):
        first_line = view.font_36.render(
            "Current Level: " + str(self.statistics.current_level) + "    Plays made: " + str(
                self.statistics.plays_done) + "   Hints Used: " + str(
                self.statistics.hints_used) + "    Time Elapsed: " + str(self.statistics.time_elapsed()),
            True, (255, 255, 255))
        view.screen.blit(first_line, (view.width // 20, view.height // 50))

    @property
    def statistics(self):
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        self._statistics = value
