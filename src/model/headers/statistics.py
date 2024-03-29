import time


class Statistics:
    def __init__(self):
        self._iterations = 0
        self._starting_time_stamp = time.time()
        self._current_time_stamp = self._starting_time_stamp
        self._current_depth = 0
        self._visited_queue_length = 0
        self._queue_length = 0
        self._current_level = 0
        self._plays_missing = 0
        self._plays_done = 0
        self._hints_used = 0

    def time_elapsed(self):
        return round(self._current_time_stamp - self._starting_time_stamp)

    @property
    def iterations(self):
        return self._iterations

    @iterations.setter
    def iterations(self, value):
        self._iterations = value

    @property
    def current_time_stamp(self):
        return self._current_time_stamp

    @current_time_stamp.setter
    def current_time_stamp(self, value):
        self._current_time_stamp = value

    @property
    def current_depth(self):
        return self._current_depth

    @current_depth.setter
    def current_depth(self, value):
        self._current_depth = value

    @property
    def visited_queue_length(self):
        return self._visited_queue_length

    @visited_queue_length.setter
    def visited_queue_length(self, value):
        self._visited_queue_length = value

    @property
    def queue_length(self):
        return self._queue_length

    @queue_length.setter
    def queue_length(self, value):
        self._queue_length = value

    @property
    def current_level(self):
        return self._current_level

    @current_level.setter
    def current_level(self, value):
        self._current_level = value

    @property
    def plays_missing(self):
        return self._plays_missing

    @plays_missing.setter
    def plays_missing(self, value):
        self._plays_missing = value

    @property
    def plays_done(self):
        return self._plays_done

    @plays_done.setter
    def plays_done(self, value):
        self._plays_done = value

    @property
    def hints_used(self):
        return self._hints_used

    @hints_used.setter
    def hints_used(self, value):
        self._hints_used = value
