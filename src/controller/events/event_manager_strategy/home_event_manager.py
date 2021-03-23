class HomeEventManager:
    def __init__(self, model):
        self._model = model

    def handle_mouse_event(self, event):
        for button in self.model.buttons:
            if button.rect.collidepoint(event.pos):
                return button

        return None

    @property
    def model(self):
        return self._model
