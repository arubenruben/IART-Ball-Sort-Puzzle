def is_same_color(ball1, ball2):
    return ball1.value == ball2.value


def is_solved(tubes):
    for tube in tubes:
        if not tube.is_solved():
            return False
    return True
