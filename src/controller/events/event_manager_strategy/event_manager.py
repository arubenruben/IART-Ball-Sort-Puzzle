class EventManager:
    def __init__(self, animation_manager, test_tubes):
        self._animation_manager = animation_manager
        self._test_tubes = test_tubes

    def handle_mouse_event(self, event):

        if self._animation_manager.animation_pending:
            return

        test_tube_that_collide = None

        for test_tube in self._test_tubes:
            if test_tube.rect.collidepoint(event.pos):
                test_tube_that_collide = test_tube
                break

        return self._animation_manager.process_collision(test_tube_that_collide)
