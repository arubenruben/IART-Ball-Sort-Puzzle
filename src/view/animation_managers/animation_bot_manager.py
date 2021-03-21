from time import sleep

from src.view.animation_managers.animation_manager import AnimationManager


class AnimationBotManager(AnimationManager):
    def __init__(self):
        self._animation_pending = False
        self._test_tube_origin = None
        self._test_tube_destination = None
        self._model = None
        self._node = None

    def execute_move_animation(self, node, model):
        if self._animation_pending:
            return
        self._model = model
        self._node = node

        if node.parent is None:
            return

        self.animation_pending = True
        parent = node.parent

        move = node.operator

        self._model.state = parent.state
        self._test_tube_origin = parent.state.test_tubes[move.origin_index]
        self._test_tube_destination = parent.state.test_tubes[move.destination_index]
        self._test_tube_origin.set_animation_up(self.up_animation_done)


    def up_animation_done(self):
        self._test_tube_origin.set_animation_between_tubes(self._test_tube_destination.rect, self.move_animation_done)


    def move_animation_done(self):
        self.animation_pending = False
        self._model.state = self._node.state


    @property
    def animation_pending(self):
        return self._animation_pending


    @animation_pending.setter
    def animation_pending(self, value):
        self._animation_pending = value
