import time

from src.model.drawable import Drawable
from src.model.headers.statistics import Statistics


class BotSearchingHeader(Drawable):
    def __init__(self, algorithm_name):
        self._statistics = Statistics()
        self._algorithm_name = algorithm_name

    def update(self):
        self.statistics.iterations += 1
        self.statistics.current_time_stamp = time.time()

    def draw(self, view):
        offset_between_lines = view.height // 40
        first_line = view.font_36.render("Searching Using Algorithm: " + self._algorithm_name, True, (255, 255, 255))
        view.screen.blit(first_line, (view.width // 2 - first_line.get_width() // 2, offset_between_lines))

        second_line = view.font_36.render("Time Elapsed: " + str(
            self.statistics.time_elapsed()) + "   Number of iterations: " + str(self.statistics.iterations), True,
                                          (255, 255, 255))

        view.screen.blit(second_line, (
            (view.width // 2 - second_line.get_width() // 2, first_line.get_height() + offset_between_lines * 2))),

        third_line = view.font_36.render("Visited Nodes: " + str(
            self.statistics.visited_queue_length) + "   Auxiliary Queue Size: " + str(
            str(self.statistics.queue_length)) + "   Current Depth: " + str(self.statistics.current_depth), True,
                                         (255, 255, 255))

        view.screen.blit(third_line, (
            view.width // 2 - third_line.get_width() // 2,
            first_line.get_height() + second_line.get_height() + offset_between_lines * 3))

    @property
    def statistics(self):
        return self._statistics

    @property
    def algorithm_name(self):
        return self._algorithm_name
