from model.elements.ball import Ball


def convert_raw_matrix_to_balls(raw_list, tube_position):
    response = []

    for i in range(len(raw_list)):

        if raw_list[i] == 0:
            break

        response.append(Ball(tube_position, raw_list[i], i))

    return response
