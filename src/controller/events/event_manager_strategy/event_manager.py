class EventManager:
    def __init__(self, animation_manager, test_tubes):
        self._animation_manager = animation_manager
        self._test_tubes = test_tubes

    def handle_mouse_event(self, event):

        if self._animation_manager.animation_pending:
            return

        for test_tube in self._test_tubes:
            if test_tube.rect.collidepoint(event.pos):
                return self._animation_manager.process_collision(test_tube)

        return None
