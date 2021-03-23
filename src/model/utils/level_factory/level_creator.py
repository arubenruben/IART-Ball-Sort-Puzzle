import math

import pygame

from src.model.elements.test_tube import TestTube
from src.model.utils.raw_ball_converter import convert_raw_matrix_to_balls


class LevelCreator:

    def create(self, level_number, screen_dimension):
        screen_width, screen_height = screen_dimension
        maximum_number_tubes_per_row = 5
        response = []

        if level_number == 1:
            raw_matrix = [
                [3, 2, 1, 2],
                [2, 3, 1, 1],
                [1, 2, 3, 3],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]

        elif level_number == 2:

            raw_matrix = [
                [1, 5, 2, 2],
                [3, 4, 7, 3],
                [5, 7, 5, 6],
                [4, 2, 5, 4],
                [2, 7, 1, 3],
                [6, 6, 1, 7],
                [3, 6, 1, 4],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
        elif level_number == 3:

            raw_matrix = [
                [7, 6, 1, 4],
                [2, 1, 6, 1],
                [3, 3, 2, 4],
                [3, 2, 6, 5],
                [7, 4, 5, 3],
                [5, 5, 2, 4],
                [7, 7, 6, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]

        elif level_number == 4:
            return [

            ]

        elif level_number == 5:
            return [

            ]
        elif level_number == 6:
            return [

            ]
        elif level_number == 7:
            return [

            ]
        elif level_number == 8:
            return [

            ]
        elif level_number == 9:
            return [

            ]
        elif level_number == 10:
            return [

            ]
        else:
            return None

        if raw_matrix is None:
            return

        number_rows = math.ceil(len(raw_matrix) / 5)
        margin_y = math.floor(2 * screen_height / 10)
        margin_x = math.floor(2 * screen_width / 10)

        screen_width_available = screen_width - 2 * margin_x
        screen_height_available = screen_height - 2 * margin_y

        distance_between_rows = math.floor(2 * screen_height_available / 10)
        total_distance_wasted_between_rows = (number_rows - 1) * math.floor(2 * screen_height_available / 10)
        test_tube_height = math.floor((screen_height_available - total_distance_wasted_between_rows) / number_rows)

        # If it turns out the size of the tub is huge, repeat calculation with bigger capping
        if test_tube_height > (screen_height // 3):
            margin_y = math.floor(screen_height / 3)
            margin_x = math.floor(screen_width / 5)

            screen_width_available = screen_width - 2 * margin_x
            screen_height_available = screen_height - 2 * margin_y

            distance_between_rows = math.floor(2 * screen_height_available / 10)
            total_distance_wasted_between_rows = (number_rows - 1) * math.floor(2 * screen_height_available / 10)
            test_tube_height = math.floor((screen_height_available - total_distance_wasted_between_rows) / number_rows)

        test_tube_width = math.floor(screen_width_available / 10)
        ##########

        row_counter = 0
        distance_between_cols = -1

        offset_y = margin_y
        offset_x = margin_x

        for tube_counter in range(len(raw_matrix)):

            if tube_counter > 0 and tube_counter % maximum_number_tubes_per_row == 0:
                row_counter += 1
                offset_y += distance_between_rows + test_tube_height
                offset_x = margin_x

            if row_counter == number_rows - 1:
                number_cols = len(raw_matrix) - tube_counter
            else:
                number_cols = maximum_number_tubes_per_row

            if tube_counter == 0 or tube_counter > 0 and tube_counter % maximum_number_tubes_per_row == 0:
                total_space_filled_by_tubes_in_row = number_cols * test_tube_width
                total_space_available_for_distance_between_tubes = screen_width_available - total_space_filled_by_tubes_in_row
                distance_between_cols = math.floor(total_space_available_for_distance_between_tubes / (number_cols - 1))

            tube_position = pygame.Rect(
                offset_x, offset_y, test_tube_width, test_tube_height
            )
            balls = convert_raw_matrix_to_balls(raw_matrix[tube_counter], tube_position)

            response.append(
                TestTube(
                    balls,
                    tube_position
                )
            )
            offset_x += distance_between_cols + test_tube_width

        return response
