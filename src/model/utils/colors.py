import pygame

RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
YELLOW = pygame.Color(255, 255, 0)
ORANGE = pygame.Color(255, 128, 0)
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
VIOLET = pygame.Color(127, 0, 255)
LIGHT_BLUE = pygame.Color(173, 216, 230)


def color_converter(int_value):
    if int_value == 1:
        return RED
    elif int_value == 2:
        return BLUE
    elif int_value == 3:
        return YELLOW
    elif int_value == 4:
        return GREEN
    elif int_value == 5:
        return VIOLET
    elif int_value == 6:
        return ORANGE
    elif int_value == 7:
        return LIGHT_BLUE
    elif int_value == 8:
        return WHITE
    elif int_value == 9:
        return BLACK
