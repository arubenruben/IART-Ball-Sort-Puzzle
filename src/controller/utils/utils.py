def is_same_color(ball1, ball2):
    return ball1.color == ball2.color


def is_solved(state):
    for tube in state.test_tubes:
        if not tube.is_solved():
            return False
    return True
