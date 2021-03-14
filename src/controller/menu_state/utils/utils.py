def move_ball(tube1, tube2):
    tube2.balls.append(tube1.balls.pop())


def is_same_color(ball1, ball2):
    return ball1.color == ball2.color
