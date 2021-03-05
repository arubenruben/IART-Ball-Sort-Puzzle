import pygame

from src.controller.menu_state.menu_state import MenuState


class HumanPlayingState(MenuState):
    def __init__(self, game, model):
        super().__init__(game)
        self._model = model
        self._animation = None

    def run(self):

        run = True

        while run:
            self.game.clock.tick(self.game.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_event(pygame.mouse.get_pos())

            self.model.update()

            self.model.draw(self.game.screen)

        pygame.quit()

    def handle_mouse_event(self, pos):

        for test_tube in self.model.test_tubes:
            if test_tube.rect.collidepoint(pos) and self.animation is None:
                return self.perform_up_animation(test_tube)
            elif test_tube.rect.collidepoint(pos) and self.animation is not None:
                if self.animation[0] == test_tube and self.animation[1] == "up":
                    return self.perform_down_animation()
                elif self.animation[0] != test_tube and self.animation[1] == "up":
                    return self.perform_move_operation(test_tube)

    def perform_up_animation(self, test_tube):
        self.animation = (test_tube, "up")
        self.animation[0].animation_up()

    def perform_down_animation(self):
        # TODO: DANGER DANGER DANGER DANGER
        self.animation[0].animation_down()
        self.animation = None
        # TODO: DANGER DANGER DANGER DANGER
        # TODO:ISTO ESTA MAL, NAO PODE FICAR ASSIM, E SO PARA FUNCIONAR

    def perform_move_operation(self, tube_destination):
        pass

    @property
    def model(self):
        return self._model

    @property
    def animation(self):
        return self._animation

    @animation.setter
    def animation(self, value):
        self._animation = value
