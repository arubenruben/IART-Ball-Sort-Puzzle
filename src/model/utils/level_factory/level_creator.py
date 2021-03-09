import pygame
import math
from model.elements.test_tube import TestTube


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

        if raw_matrix is not None:

            margins_y = (2 * screen_height) // 5
            margins_x = (2 * screen_width) // 10

            margin_left = margins_x
            margin_top = margins_y // 2

            available_width = screen_width - margins_x
            available_height = screen_height - margins_y

            offset_between_rows = available_height // 10

            number_rows = math.ceil(len(raw_matrix) / 5)

            height_available_for_rows = available_height - (offset_between_rows * (number_rows - 1))

            test_tube_height = math.ceil(height_available_for_rows / number_rows)
            test_tube_width = math.ceil(available_width / 13)

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
                            margin_left + (i % 5) * math.ceil(2 * test_tube_width),
                            margin_top + row_counter * (test_tube_height + offset_between_rows),
                            test_tube_width,
                            test_tube_height
                        )
                    )
                )
            return response
