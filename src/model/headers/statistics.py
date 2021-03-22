import time


class Statistics:
    def __init__(self):
        self._iterations = 0
        self._starting_time_stamp = time.time()
        self._current_time_stamp = self._starting_time_stamp
        self._current_depth = 0
        self._visited_queue_length = 0
        self._queue_length = 0

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
