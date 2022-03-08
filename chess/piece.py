# Python built-in libraries
from typing import Tuple

# 3rd-party libraries
import pygame

# Custom imports
from .constants import BLACK_CANNON, BLACK_ELEPHANT, BLACK_GUARD, BLACK_HORSE, BLACK_KING, BLACK_ROOK, BLACK_SOLDIER, EMPTY, RED, RED_CANNON, RED_ELEPHANT, RED_GUARD, RED_HORSE, RED_KING, RED_ROOK, RED_SOLDIER, SQUARE_SIZE


class Piece:
    def __init__(self, row: int, col: int, color: str) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.x, self. y = self.get_pos()
        self.image = self.get_loaded_image()

    # Abstract method: Get pieces image path
    def get_loaded_image(self) -> pygame.Surface:
        raise NotImplementedError

    # Get (x,y) position based on (row,col)
    def get_pos(self) -> Tuple[int, int]:
        return self.col * SQUARE_SIZE + 17, self.row * SQUARE_SIZE + 17

    # Draw the image on the board
    def draw(self, win: pygame.Surface) -> None:
        win.blit(self.image, (self.x, self.y))

    # Change row, col and (x,y) position
    def move(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.x, self.y = self.get_pos()


class King(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_KING if self.color == RED else BLACK_KING


class Rook(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_ROOK if self.color == RED else BLACK_ROOK


class Horse(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_HORSE if self.color == RED else BLACK_HORSE


class Cannon(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_CANNON if self.color == RED else BLACK_CANNON


class Guard(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_GUARD if self.color == RED else BLACK_GUARD


class Elephant(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_ELEPHANT if self.color == RED else BLACK_ELEPHANT


class Soldier(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_SOLDIER if self.color == RED else BLACK_SOLDIER


class Empty(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return EMPTY
