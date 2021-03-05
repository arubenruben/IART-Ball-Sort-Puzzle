import pygame

from src.model.elements.test_tube import TestTube


class LevelCreator:

    def create(self, level_number, screen_dimension):
        screen_width, screen_height = screen_dimension
        # With offset of 0.1 each side

        if level_number == 1:
            number_tubs = 5
            number_rows = number_tubs // 5
            test_tube_dimensions = ((screen_width * 0.8) // 5, (screen_height * 0.8) // number_rows)
            left_offset = screen_width * 0.1
            top_offset = screen_height * 0.1

            return [
                TestTube(
                    [3, 2, 1, 2],
                    pygame.Rect((left_offset, top_offset), test_tube_dimensions)
                ),
                TestTube(
                    [2, 3, 1, 1],
                    pygame.Rect((left_offset + test_tube_dimensions[0], top_offset), test_tube_dimensions)
                ),
                TestTube(
                    [1, 2, 3, 3],
                    pygame.Rect((left_offset + test_tube_dimensions[0] * 2, top_offset), test_tube_dimensions)
                ),
                TestTube(
                    [0, 0, 0, 0],
                    pygame.Rect((left_offset + test_tube_dimensions[0] * 3, top_offset), test_tube_dimensions)
                ),
                TestTube(
                    [0, 0, 0, 0],
                    pygame.Rect((left_offset + test_tube_dimensions[0] * 4, top_offset), test_tube_dimensions)
                ),
            ]

        elif level_number == 2:
            return []
            # return [
            # TestTube([1, 5, 2, 2]),
            # TestTube([3, 4, 7, 3]),
            # TestTube([5, 7, 5, 6]),
            # TestTube([4, 2, 5, 4]),
            # TestTube([2, 7, 1, 3]),
            # TestTube([6, 6, 1, 7]),
            # TestTube([3, 6, 1, 4]),
            # TestTube([0, 0, 0, 0]),
            # TestTube([0, 0, 0, 0]),
            # ]

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
