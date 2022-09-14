
# 3rd-party libraries
import os
import sys
import pygame


WIDTH, HEIGHT = 670, 750
ROWS, COLS = 10, 9
SQUARE_SIZE = 70
OFFSET = 50

# RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW_ORANGE = (252, 174, 63)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Pieces
RED_KING = pygame.image.load(resource_path(r"assets\r-k.png"))
BLACK_KING = pygame.image.load(resource_path(r"assets\b-k.png"))
RED_ROOK = pygame.image.load(resource_path(r"assets\r-r.png"))
BLACK_ROOK = pygame.image.load(resource_path(r"assets\b-r.png"))
RED_HORSE = pygame.image.load(resource_path(r"assets\r-h.png"))
BLACK_HORSE = pygame.image.load(resource_path(r"assets\b-h.png"))
RED_CANNON = pygame.image.load(resource_path(r"assets\r-c.png"))
BLACK_CANNON = pygame.image.load(resource_path(r"assets\b-c.png"))
RED_GUARD = pygame.image.load(resource_path(r"assets\r-g.png"))
BLACK_GUARD = pygame.image.load(resource_path(r"assets\b-g.png"))
RED_ELEPHANT = pygame.image.load(resource_path(r"assets\r-e.png"))
BLACK_ELEPHANT = pygame.image.load(resource_path(r"assets\b-e.png"))
RED_SOLDIER = pygame.image.load(resource_path(r"assets\r-s.png"))
BLACK_SOLDIER = pygame.image.load(resource_path(r"assets\b-s.png"))
EMPTY = pygame.image.load(resource_path(r"assets\empty.png"))
