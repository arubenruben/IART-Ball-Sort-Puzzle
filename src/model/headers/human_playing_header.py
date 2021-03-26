import time

from src.model.drawable import Drawable
from src.model.headers.statistics import Statistics


class HumanPlayingHeader(Drawable):
    def __init__(self):
        self._statistics = Statistics()
        self._hint_time_stamp = None
        self._hint = None

    def update(self):
        self.statistics.current_time_stamp = time.time()

        if self._hint_time_stamp is not None and self.statistics.current_time_stamp - self._hint_time_stamp > 15:
            self._hint_time_stamp = None
            self._hint = None

    def draw(self, view):
        first_line = view.font_36.render(
            "Current Level: " + str(self.statistics.current_level) + "    Plays made: " + str(
                self.statistics.plays_done) + "   Hints Used: " + str(
                self.statistics.hints_used) + "    Time Elapsed: " + str(self.statistics.time_elapsed()),
            True, (255, 255, 255))
        view.screen.blit(first_line, (view.width // 20, view.height // 50))
        if self._hint is not None:
            second_line = view.font_36.render(
                "Hint: " + str(self.hint), True, (255, 255, 255))
            view.screen.blit(second_line, (view.width // 20, view.height // 10))

    @property
    def statistics(self):
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        self._statistics = value

    @property
    def hint(self):
        return self._hint

    @hint.setter
    def hint(self, value):
        self._hint = value
        self._hint_time_stamp = time.time()
