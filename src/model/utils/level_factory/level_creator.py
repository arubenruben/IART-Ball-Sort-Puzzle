import pygame

from src.model.elements.test_tube import TestTube


class LevelCreator:

    def create(self, level_number, screen_dimension):
        screen_width, screen_height = screen_dimension

        if level_number == 1:
            return [
                TestTube(
                    [3, 2, 1, 2],
                    pygame.Rect((80, screen_height // 3), (38, 180))
                ),
                TestTube(
                    [2, 3, 1, 1],
                    pygame.Rect((170, screen_height // 3), (38, 180))
                ),
                TestTube(
                    [1, 2, 3, 3],
                    pygame.Rect((280, screen_height // 3), (38, 180))
                ),
                TestTube(
                    [0, 0, 0, 0],
                    pygame.Rect((390, screen_height // 3), (38, 180))
                ),
                TestTube(
                    [0, 0, 0, 0],
                    pygame.Rect((480, screen_height // 3), (38, 180))
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
