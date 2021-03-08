class EventManager:
    def __init__(self, model):
        self._model = model

    def handle_mouse_event(self, pos):
        pass

    @property
    def model(self):
        return self._model
