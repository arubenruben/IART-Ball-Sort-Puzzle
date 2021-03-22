import os

import pygame

from src.model.drawable import Drawable
from src.model.elements.ball import Ball


class TestTube(Drawable):

    def __init__(self, balls, rect):
        self._rect = rect
        self._balls = balls
        self._capacity = 4

        self._animating_up = False
        self._animating_down = False
        self._animating_move = False
        self._speed_y = 5
        self._speed_x = 5
        self._callback = None
        self._destination_rect = None
        self._original_ball_position = None

        self._background_image = pygame.transform.scale(
            pygame.image.load(os.path.join('../', 'assets', 'img', 'test_tube.png')),
            (rect.width, rect.height))

    def update(self):
        if self.animating_up:
            return self.animate_up()
        if self.animating_down:
            return self.animate_down()
        if self.animating_move:
            return self.animate_between_tubes()

    def draw(self, view):
        view.screen.blit(self.background_image, self.rect)
        for ball in self._balls:
            ball.draw(view)

    def animate_up(self):
        ball = self.get_first_ball()

        if ball.rect.top <= self.rect.top - self.rect.height // 4:
            self.reset_animations()
            self.callback()
        else:
            ball.rect = ball.rect.move(0, -self.speed_y)

    def animate_down(self):
        ball = self.get_first_ball()

        if ball.rect.top >= self.original_ball_position.bottom - 8 * self.speed_y:
            ball.rect = self.original_ball_position.copy()
            self.reset_animations()
            self.callback()
        else:
            ball.rect = ball.rect.move(0, self.speed_y)

    # Todo:Move Animation
    def animate_between_tubes(self):
        ball = self.get_first_ball()
        acceptance_offset = 10

        if (ball.rect.center[0] != self.destination_rect.center[0]) and (
                ball.rect.center[0] >= self.destination_rect.center[0] - acceptance_offset) and (
                ball.rect.center[0] <= self.destination_rect.center[0] + acceptance_offset):
            current_y = ball.rect.y
            ball.rect.center = self.destination_rect.center
            ball.rect.y = current_y
        elif ball.rect.center[0] > self.destination_rect.center[0]:
            ball.rect = ball.rect.move(-self.speed_x, 0)
            return
        elif ball.rect.center[0] < self.destination_rect.center[0]:
            ball.rect = ball.rect.move(self.speed_x, 0)
            return

        if (ball.rect.bottom > self.destination_rect.top - acceptance_offset) and (
                ball.rect.bottom < self.destination_rect.top + acceptance_offset):
            self.reset_animations()
            self.callback()
        elif ball.rect.bottom > self.destination_rect.top:
            ball.rect = ball.rect.move(0, -self.speed_y)
        elif ball.rect.bottom < self.destination_rect.top:
            ball.rect = ball.rect.move(0, self.speed_y)

    # Todo:Refactor return none

    def get_first_ball(self):
        if len(self._balls) > 0:
            return self._balls[len(self._balls) - 1]
        return None

    def is_full(self):
        return len(self._balls) == self._capacity

    def is_empty(self):
        return len(self._balls) == 0

    def is_solved(self):

        if len(self._balls) == 0:
            return True

        if len(self._balls) < self._capacity:
            return False

        start_ball = self._balls[0]

        for i in range(len(self._balls)):
            if self._balls[i].value != start_ball.value:
                return False

        return True

    # Getter and Setters
    def insert_ball(self, ball):
        self._balls.append(Ball(self.rect, ball.value, len(self._balls)))

    def pop_ball(self):
        if len(self._balls) > 0:
            return self._balls.pop()
        return None

    @property
    def background_image(self):
        return self._background_image

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, value):
        self._rect = value

    @property
    def speed_x(self):
        return self._speed_x

    @property
    def speed_y(self):
        return self._speed_y

    @property
    def animating_up(self):
        return self._animating_up

    @animating_up.setter
    def animating_up(self, value):
        self._animating_up = value

    @property
    def animating_down(self):
        return self._animating_down

    @animating_down.setter
    def animating_down(self, value):
        self._animating_down = value

    @property
    def animating_move(self):
        return self._animating_move

    @animating_move.setter
    def animating_move(self, value):
        self._animating_move = value

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value):
        self._callback = value

    @property
    def destination_rect(self):
        return self._destination_rect

    @destination_rect.setter
    def destination_rect(self, value):
        self._destination_rect = value

    @property
    def original_ball_position(self):
        return self._original_ball_position

    @original_ball_position.setter
    def original_ball_position(self, value):
        self._original_ball_position = value

    # Animations
    def set_animation_up(self, callback):
        ball = self.get_first_ball()
        self.callback = callback
        self.animating_up = True
        self.original_ball_position = ball.rect.copy()

    def set_animation_down(self, callback):
        self.callback = callback
        self.animating_down = True

    def set_animation_between_tubes(self, destination_rect, callback):
        self.destination_rect = destination_rect
        self.callback = callback
        self.animating_move = True

    def reset_animations(self):
        self.animating_up = False
        self.animating_down = False
        self.animating_move = False

    def get_raw_balls(self):
        aux_list = []
        for ball in self._balls:
            aux_list.append(ball.value)

        return aux_list

    def __eq__(self, other):
        if len(self._balls) != len(other._balls):
            return False

        for i in range(len(self._balls)):
            if self._balls[i].value != other._balls[i].value:
                return False

        return True
