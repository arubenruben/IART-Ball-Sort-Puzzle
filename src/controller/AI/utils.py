def move_ball(tube1, tube2):
    tube2.balls.append(tube1.balls.pop())


def is_move_possible(tube1, tube2):
    return (not tube1.isEmpty() and not tube2.isFull() and not is_tube_solved(tube1)
            and (tube2.isEmpty() or is_same_color(tube1.getFirstBall(), tube2.getFirstBall())))


# Using Aux Set to remove duplicates and if the number of balls is just 1 or 0 is finished
def is_tube_solved(tube):
    if len(set(tube.balls)) > 1 or len(tube.balls) == 1:
        return False
    else:
        return True


def is_solved(tubes):
    for tube in tubes:
        if not is_tube_solved(tube):
            return False
    return True


def is_same_color(ball1, ball2):
    return ball1.color == ball2.color
