def is_same_color(ball1, ball2):
    if ball1.value == 0 or ball2.value == 0:
        return True

    if ball1.value == ball2.value:
        return True

    return False


def is_solved(tubes):
    for tube in tubes:
        if not tube.is_solved():
            return False
    return True
