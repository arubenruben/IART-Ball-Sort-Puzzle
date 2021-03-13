from src.model.move import Move


class EventManager:
    def __init__(self, state, animation_manager):
        self._state = state
        self._animation_manager = animation_manager

    def handle_mouse_event(self, event):

        if self.animation_manager.animation_pending:
            return

        test_tube_that_collide = None

        for test_tube in self.state:
            if test_tube.rect.collidepoint(event.pos):
                test_tube_that_collide = test_tube
                break

        return self.animation_manager.process_collision(test_tube_that_collide)

    @property
    def state(self):
        return self._state

    @property
    def animation_manager(self):
        return self._animation_manager
