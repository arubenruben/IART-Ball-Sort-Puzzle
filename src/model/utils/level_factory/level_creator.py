import math

import pygame

from src.model.elements.test_tube import TestTube


class LevelCreator:

    def create(self, level_number, screen_dimension):
        screen_width, screen_height = screen_dimension
        raw_matrix = None
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

            return [

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

        if raw_matrix is None:
            return

        response = []

        number_rows = math.ceil(len(raw_matrix) / 5)
        margin_y = math.floor(2 * screen_height / 10)
        margin_x = math.floor(2 * screen_width / 10)

        screen_width_available = screen_width - 2 * margin_x
        screen_height_available = screen_height - 2 * margin_y

        distance_between_rows = math.floor(2 * screen_height_available / 10)
        total_distance_wasted_between_rows = (number_rows - 1) * math.floor(2 * screen_height_available / 10)
        test_tube_height = math.floor((screen_height_available - total_distance_wasted_between_rows) / number_rows)
        ##########

        test_tube_width = math.ceil(screen_width_available / 13)

        response = []
        row_counter = 0
        left_offset_counter = 0

        for i in range(len(raw_matrix)):
            if i > 0 and i % 5 == 0:
                row_counter += 1
                left_offset_counter = 0

            response.append(
                TestTube(
                    raw_matrix[i],
                    pygame.Rect(
                        margin_x + (i % 5) * math.ceil(2 * test_tube_width),
                        margin_y + row_counter * (test_tube_height + distance_between_rows),
                        test_tube_width,
                        test_tube_height
                    )
                )
            )
        return response
