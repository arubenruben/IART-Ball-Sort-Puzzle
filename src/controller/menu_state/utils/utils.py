def move_ball(tube1, tube2):
    tube2.balls.append(tube1.balls.pop())


def is_move_possible(tube1, tube2):
    return (not tube1.is_empty() and not tube2.is_full() and not tube1.is_solved()
            and (tube2.is_empty() or is_same_color(tube1.get_first_ball(), tube2.get_first_ball())))


def is_same_color(ball1, ball2):
    return ball1.color == ball2.color

