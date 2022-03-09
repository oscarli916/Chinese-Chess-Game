# Python built-in libraries
from typing import Tuple

# 3rd-party libraries
import pygame

# Custom imports
from .constants import BLACK, BLACK_CANNON, BLACK_ELEPHANT, BLACK_GUARD, BLACK_HORSE, BLACK_KING, BLACK_ROOK, BLACK_SOLDIER, COLS, EMPTY, RED, RED_CANNON, RED_ELEPHANT, RED_GUARD, RED_HORSE, RED_KING, RED_ROOK, RED_SOLDIER, ROWS, SQUARE_SIZE


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

    # Abstract method: Get pieces valid move
    def get_valid_moves(self, board) -> dict:
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

    def get_valid_moves(self, board) -> dict:
        moves = {}
        if self.color == RED:
            if self.row > 7 and board[self.row - 1][self.col].color != self.color:
                moves[(self.row - 1, self.col)] = 1
            if self.row < ROWS - 1 and board[self.row + 1][self.col].color != self.color:
                moves[(self.row + 1, self.col)] = 1
        elif self.color == BLACK:
            if self.row > 0 and board[self.row - 1][self.col].color != self.color:
                moves[(self.row - 1, self.col)] = 1
            if self.row < 2 and board[self.row + 1][self.col].color != self.color:
                moves[(self.row + 1, self.col)] = 1

        if self.col > 3 and board[self.row][self.col - 1].color != self.color:
            moves[(self.row, self.col - 1)] = 1
        if self.col < 5 and board[self.row][self.col + 1].color != self.color:
            moves[(self.row, self.col + 1)] = 1
        return moves


class Rook(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_ROOK if self.color == RED else BLACK_ROOK

    def get_valid_moves(self, board) -> dict:
        moves = {}
        # Check forward valid moves
        for row in range(self.row - 1, -1, -1):
            if isinstance(board[row][self.col], Empty):
                moves[(row, self.col)] = 1
            elif board[row][self.col].color != self.color:
                moves[(row, self.col)] = 1
                break
            else:
                break
        # Check backward valid moves
        for row in range(self.row + 1, ROWS):
            if isinstance(board[row][self.col], Empty):
                moves[(row, self.col)] = 1
            elif board[row][self.col].color != self.color:
                moves[(row, self.col)] = 1
                break
            else:
                break
        # Check left valid moves
        for col in range(self.col - 1, -1, -1):
            if isinstance(board[self.row][col], Empty):
                moves[(self.row, col)] = 1
            elif board[self.row][col].color != self.color:
                moves[(self.row, col)] = 1
                break
            else:
                break
        # Check right valid moves
        for col in range(self.col + 1, COLS):
            if isinstance(board[self.row][col], Empty):
                moves[(self.row, col)] = 1
            elif board[self.row][col].color != self.color:
                moves[(self.row, col)] = 1
                break
            else:
                break

        return moves


class Horse(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_HORSE if self.color == RED else BLACK_HORSE

    def get_valid_moves(self, board) -> dict:
        moves = {}
        # Check forward valid moves
        if self.row - 1 > 0 and isinstance(board[self.row - 1][self.col], Empty):
            if self.col - 1 >= 0 and board[self.row - 2][self.col - 1].color != self.color:
                moves[(self.row - 2, self.col - 1)] = 1
            if self.col + 1 < COLS and board[self.row - 2][self.col + 1].color != self.color:
                moves[(self.row - 2, self.col + 1)] = 1
        # Check backward valid moves
        if self.row + 1 < ROWS - 1 and isinstance(board[self.row + 1][self.col], Empty):
            if self.col - 1 >= 0 and board[self.row + 2][self.col - 1].color != self.color:
                moves[(self.row + 2, self.col - 1)] = 1
            if self.col + 1 < COLS and board[self.row + 2][self.col + 1].color != self.color:
                moves[(self.row + 2, self.col + 1)] = 1
        # Check left valid moves
        if self.col - 1 > 0 and isinstance(board[self.row][self.col - 1], Empty):
            if self.row - 1 >= 0 and board[self.row - 1][self.col - 2].color != self.color:
                moves[(self.row - 1, self.col - 2)] = 1
            if self.row + 1 < ROWS and board[self.row + 1][self.col - 2].color != self.color:
                moves[(self.row + 1, self.col - 2)] = 1
        # Check right valid moves
        if self.col + 1 < COLS - 1 and isinstance(board[self.row][self.col + 1], Empty):
            if self.row - 1 >= 0 and board[self.row - 1][self.col + 2].color != self.color:
                moves[(self.row - 1, self.col + 2)] = 1
            if self.row + 1 < ROWS and board[self.row + 1][self.col + 2].color != self.color:
                moves[(self.row + 1, self.col + 2)] = 1
        return moves


class Cannon(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_CANNON if self.color == RED else BLACK_CANNON

    def get_valid_moves(self, board) -> dict:
        moves = {}
        # Check forward valid moves
        for row in range(self.row - 1, -1, -1):
            if isinstance(board[row][self.col], Empty):
                moves[(row, self.col)] = 1
            else:
                for row2 in range(row - 1, -1, -1):
                    if not isinstance(board[row2][self.col], Empty):
                        if board[row2][self.col].color != self.color:
                            moves[(row2, self.col)] = 1
                        break
                break
        # Check backward valid moves
        for row in range(self.row + 1, ROWS):
            if isinstance(board[row][self.col], Empty):
                moves[(row, self.col)] = 1
            else:
                for row2 in range(row + 1, ROWS):
                    if not isinstance(board[row2][self.col], Empty):
                        if board[row2][self.col].color != self.color:
                            moves[(row2, self.col)] = 1
                        break
                break
        # Check left valid moves
        for col in range(self.col - 1, -1, -1):
            if isinstance(board[self.row][col], Empty):
                moves[(self.row, col)] = 1
            else:
                for col2 in range(col - 1, -1, -1):
                    if not isinstance(board[self.row][col2], Empty):
                        if board[self.row][col2].color != self.color:
                            moves[(self.row, col2)] = 1
                        break
                break
        # Check right valid moves
        for col in range(self.col + 1, COLS):
            if isinstance(board[self.row][col], Empty):
                moves[(self.row, col)] = 1
            else:
                for col2 in range(col + 1, COLS):
                    if not isinstance(board[self.row][col2], Empty):
                        if board[self.row][col2].color != self.color:
                            moves[(self.row, col2)] = 1
                        break
                break
        return moves


class Guard(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_GUARD if self.color == RED else BLACK_GUARD

    def get_valid_moves(self, board) -> dict:
        color_map = {RED: 8, BLACK: 1}
        moves = {}
        if (self.col == 3 or self.col == 5) and board[color_map[self.color]][4].color != self.color:
            moves[(color_map[self.color], 4)] = 1
        elif self.col == 4:
            if board[color_map[self.color] - 1][3].color != self.color:
                moves[(color_map[self.color] - 1, 3)] = 1
            if board[color_map[self.color] - 1][5].color != self.color:
                moves[(color_map[self.color] - 1, 5)] = 1
            if board[color_map[self.color] + 1][3].color != self.color:
                moves[(color_map[self.color] + 1, 3)] = 1
            if board[color_map[self.color] + 1][5].color != self.color:
                moves[(color_map[self.color] + 1, 5)] = 1
        return moves


class Elephant(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_ELEPHANT if self.color == RED else BLACK_ELEPHANT

    def get_valid_moves(self, board) -> dict:
        moves = {}
        # Check RED valid moves
        if self.color == RED:
            if self.row == ROWS - 1:
                if self.col == 2:
                    if board[7][0].color != self.color and isinstance(board[8][1], Empty):
                        moves[(7, 0)] = 1
                    if board[7][4].color != self.color and isinstance(board[8][3], Empty):
                        moves[(7, 4)] = 1
                elif self.col == 6:
                    if board[7][8].color != self.color and isinstance(board[8][7], Empty):
                        moves[(7, 8)] = 1
                    if board[7][4].color != self.color and isinstance(board[8][5], Empty):
                        moves[(7, 4)] = 1

            elif self.row == 7:
                if self.col == 0:
                    if board[5][2].color != self.color and isinstance(board[6][1], Empty):
                        moves[(5, 2)] = 1
                    if board[9][2].color != self.color and isinstance(board[8][1], Empty):
                        moves[(9, 2)] = 1
                elif self.col == 4:
                    if board[5][2].color != self.color and isinstance(board[6][3], Empty):
                        moves[(5, 2)] = 1
                    if board[5][6].color != self.color and isinstance(board[6][5], Empty):
                        moves[(5, 6)] = 1
                    if board[9][2].color != self.color and isinstance(board[8][3], Empty):
                        moves[(9, 2)] = 1
                    if board[9][6].color != self.color and isinstance(board[8][5], Empty):
                        moves[(9, 6)] = 1
                elif self.col == 8:
                    if board[5][6].color != self.color and isinstance(board[6][7], Empty):
                        moves[(5, 6)] = 1
                    if board[9][6].color != self.color and isinstance(board[8][7], Empty):
                        moves[(9, 6)] = 1
            elif self.row == 5:
                if self.col == 2:
                    if board[7][0].color != self.color and isinstance(board[6][1], Empty):
                        moves[(7, 0)] = 1
                    if board[7][4].color != self.color and isinstance(board[6][3], Empty):
                        moves[(7, 4)] = 1
                elif self.col == 6:
                    if board[7][8].color != self.color and isinstance(board[6][7], Empty):
                        moves[(7, 8)] = 1
                    if board[7][4].color != self.color and isinstance(board[6][5], Empty):
                        moves[(7, 4)] = 1
        # Check BLACK valid moves
        else:
            if self.row == 0:
                if self.col == 2:
                    if board[2][0].color != self.color and isinstance(board[1][1], Empty):
                        moves[(2, 0)] = 1
                    if board[2][4].color != self.color and isinstance(board[1][3], Empty):
                        moves[(2, 4)] = 1
                elif self.col == 6:
                    if board[2][8].color != self.color and isinstance(board[1][7], Empty):
                        moves[(2, 8)] = 1
                    if board[2][4].color != self.color and isinstance(board[1][5], Empty):
                        moves[(2, 4)] = 1
            elif self.row == 2:
                if self.col == 0:
                    if board[0][2].color != self.color and isinstance(board[1][1], Empty):
                        moves[(0, 2)] = 1
                    if board[4][2].color != self.color and isinstance(board[3][1], Empty):
                        moves[(4, 2)] = 1
                elif self.col == 4:
                    if board[0][2].color != self.color and isinstance(board[1][3], Empty):
                        moves[(0, 2)] = 1
                    if board[0][6].color != self.color and isinstance(board[1][5], Empty):
                        moves[(0, 6)] = 1
                    if board[4][2].color != self.color and isinstance(board[3][3], Empty):
                        moves[(4, 2)] = 1
                    if board[4][6].color != self.color and isinstance(board[3][5], Empty):
                        moves[(4, 6)] = 1
                elif self.col == 8:
                    if board[0][6].color != self.color and isinstance(board[1][7], Empty):
                        moves[(0, 6)] = 1
                    if board[4][6].color != self.color and isinstance(board[3][7], Empty):
                        moves[(4, 6)] = 1
            elif self.row == 4:
                if self.col == 2:
                    if board[2][0].color != self.color and isinstance(board[3][1], Empty):
                        moves[(2, 0)] = 1
                    if board[2][4].color != self.color and isinstance(board[3][3], Empty):
                        moves[(2, 4)] = 1
                elif self.col == 6:
                    if board[2][8].color != self.color and isinstance(board[3][7], Empty):
                        moves[(2, 8)] = 1
                    if board[2][4].color != self.color and isinstance(board[3][5], Empty):
                        moves[(2, 4)] = 1
        return moves


class Soldier(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return RED_SOLDIER if self.color == RED else BLACK_SOLDIER

    def get_valid_moves(self, board) -> dict:
        moves = {}
        # Check RED valid moves
        if self.color == RED:
            if self.row > 0 and board[self.row - 1][self.col].color != self.color:
                moves[(self.row - 1, self.col)] = 1

            if self.row < 5:
                if self.col > 0 and board[self.row][self.col - 1].color != self.color:
                    moves[(self.row, self.col - 1)] = 1
                if self.col < COLS - 1 and board[self.row][self.col + 1].color != self.color:
                    moves[(self.row, self.col + 1)] = 1

        # Check BLACK valid moves
        elif self.color == BLACK:
            if self.row < ROWS - 1 and board[self.row + 1][self.col].color != self.color:
                moves[(self.row + 1, self.col)] = 1

            if self.row > 4:
                if self.col > 0 and board[self.row][self.col - 1].color != self.color:
                    moves[(self.row, self.col - 1)] = 1
                if self.col < COLS - 1 and board[self.row][self.col + 1].color != self.color:
                    moves[(self.row, self.col + 1)] = 1

        return moves


class Empty(Piece):
    def __init__(self, row: int, col: int, color: str) -> None:
        super().__init__(row, col, color)

    def get_loaded_image(self) -> pygame.Surface:
        return EMPTY
