# Python built-in libraries
from typing import Tuple

# 3rd-party libraries
import pygame

# Custom imports
from .constants import SQUARE_SIZE


class Piece:
    def __init__(self, row: int, col: int, color: str) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.x, self. y = self.get_pos()
        self.image = pygame.image.load(self.get_image_path())

    # Abstract method: Get pieces image path
    def get_image_path(self) -> None:
        raise NotImplementedError

    # Get (x,y) position based on (row,col)
    def get_pos(self) -> Tuple[int, int]:
        return self.col * SQUARE_SIZE + 20, self.row * SQUARE_SIZE + 20

    # Draw the image on the board
    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.image, (self.x, self.y))


class King(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_image_path(self) -> str:
        return "chess/images/r-k.png" if self.color == "r" else "chess/images/b-k.png"


class Rook(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_image_path(self) -> str:
        return "chess/images/r-r.png" if self.color == "r" else "chess/images/b-r.png"


class Horse(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_image_path(self) -> str:
        return "chess/images/r-h.png" if self.color == "r" else "chess/images/b-h.png"


class Cannon(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_image_path(self) -> str:
        return "chess/images/r-c.png" if self.color == "r" else "chess/images/b-c.png"


class Guard(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_image_path(self) -> str:
        return "chess/images/r-g.png" if self.color == "r" else "chess/images/b-g.png"


class Elephant(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_image_path(self) -> str:
        return "chess/images/r-e.png" if self.color == "r" else "chess/images/b-e.png"


class Soldier(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_image_path(self) -> str:
        return "chess/images/r-s.png" if self.color == "r" else "chess/images/b-s.png"
