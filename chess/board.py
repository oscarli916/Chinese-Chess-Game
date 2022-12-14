
# 3rd-party libraries
import pygame

# Custom imports
from chess.piece import Cannon, Elephant, Empty, Guard, Horse, King, Piece, Rook, Soldier
from .constants import BLACK, COLS, HEIGHT, OFFSET, RED, ROWS, SQUARE_SIZE, WHITE, WIDTH, YELLOW_ORANGE


class Board:
    def __init__(self) -> None:
        self.board: list = []
        self.red_left = self.black_left = 16
        self.red_kings = self.black_kings = 1
        self.create_board()

    # Draw backgroun lines
    def draw_squares(self, win: pygame.Surface) -> None:
        # Fill background color
        win.fill(YELLOW_ORANGE)
        # Rows line
        for row in range(ROWS):
            pygame.draw.line(win, BLACK, (OFFSET, row * SQUARE_SIZE + OFFSET),
                             (OFFSET + SQUARE_SIZE * (COLS - 1), row * SQUARE_SIZE + OFFSET), 2)
        # Cols line
        for col in range(COLS):
            pygame.draw.line(win, BLACK, (col * SQUARE_SIZE + OFFSET, OFFSET),
                             (col * SQUARE_SIZE + OFFSET, OFFSET + SQUARE_SIZE * (ROWS - 1)), 2)
        # Cross line
        pygame.draw.line(win, BLACK, (260, 50), (400, 190), 2)
        pygame.draw.line(win, BLACK, (400, 50), (260, 190), 2)
        pygame.draw.line(win, BLACK, (260, 680), (400, 540), 2)
        pygame.draw.line(win, BLACK, (400, 680), (260, 540), 2)
        # Remove middle line
        for col in range(1, COLS - 1):
            pygame.draw.line(win, YELLOW_ORANGE, (col * SQUARE_SIZE + OFFSET, 330),
                             (col * SQUARE_SIZE + OFFSET, 330 + SQUARE_SIZE), 2)

    # Add Pieces to the board
    def create_board(self) -> None:
        self.board.append([Rook(0, 0, BLACK), Horse(0, 1, BLACK), Elephant(0, 2, BLACK), Guard(0, 3, BLACK), King(
            0, 4, BLACK), Guard(0, 5, BLACK), Elephant(0, 6, BLACK), Horse(0, 7, BLACK), Rook(0, 8, BLACK)])
        self.board.append([Empty(1, 0, WHITE), Empty(1, 1, WHITE), Empty(1, 2, WHITE), Empty(1, 3, WHITE), Empty(
            1, 4, WHITE), Empty(1, 5, WHITE), Empty(1, 6, WHITE), Empty(1, 7, WHITE), Empty(1, 8, WHITE)])
        self.board.append([Empty(2, 0, WHITE), Cannon(2, 1, BLACK), Empty(2, 2, WHITE), Empty(2, 3, WHITE), Empty(
            2, 4, WHITE), Empty(2, 5, WHITE), Empty(2, 6, WHITE), Cannon(2, 7, BLACK), Empty(2, 8, WHITE)])
        self.board.append([Soldier(3, 0, BLACK), Empty(3, 1, WHITE), Soldier(3, 2, BLACK), Empty(3, 3, WHITE), Soldier(
            3, 4, BLACK), Empty(3, 5, WHITE), Soldier(3, 6, BLACK), Empty(3, 7, WHITE), Soldier(3, 8, BLACK)])
        self.board.append([Empty(4, 0, WHITE), Empty(4, 1, WHITE), Empty(4, 2, WHITE), Empty(4, 3, WHITE), Empty(
            4, 4, WHITE), Empty(4, 5, WHITE), Empty(4, 6, WHITE), Empty(4, 7, WHITE), Empty(4, 8, WHITE)])
        self.board.append([Empty(5, 0, WHITE), Empty(5, 1, WHITE), Empty(5, 2, WHITE), Empty(5, 3, WHITE), Empty(
            5, 4, WHITE), Empty(5, 5, WHITE), Empty(5, 6, WHITE), Empty(5, 7, WHITE), Empty(5, 8, WHITE)])
        self.board.append([Soldier(6, 0, RED), Empty(6, 1, WHITE), Soldier(6, 2, RED), Empty(6, 3, WHITE), Soldier(
            6, 4, RED), Empty(6, 5, WHITE), Soldier(6, 6, RED), Empty(6, 7, WHITE), Soldier(6, 8, RED)])
        self.board.append([Empty(7, 0, WHITE), Cannon(7, 1, RED), Empty(7, 2, WHITE), Empty(7, 3, WHITE), Empty(
            7, 4, WHITE), Empty(7, 5, WHITE), Empty(7, 6, WHITE), Cannon(7, 7, RED), Empty(7, 8, WHITE)])
        self.board.append([Empty(8, 0, WHITE), Empty(8, 1, WHITE), Empty(8, 2, WHITE), Empty(8, 3, WHITE), Empty(
            8, 4, WHITE), Empty(8, 5, WHITE), Empty(8, 6, WHITE), Empty(8, 7, WHITE), Empty(8, 8, WHITE)])
        self.board.append([Rook(9, 0, RED), Horse(9, 1, RED), Elephant(9, 2, RED), Guard(9, 3, RED), King(
            9, 4, RED), Guard(9, 5, RED), Elephant(9, 6, RED), Horse(9, 7, RED), Rook(9, 8, RED)])

    # Draw the board
    def draw(self, win: pygame.Surface) -> None:
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                self.board[row][col].draw(win)

    def move(self, piece: Piece, row: int, col: int) -> None:
        # Change the piece in the board
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        # Change the piece attribute
        piece.move(row, col)

    # Get a piece on the board based on (row,col)
    def get_piece(self, row: int, col: int) -> Piece:
        return self.board[row][col]

    def get_valid_moves(self, piece: Piece) -> dict:
        return piece.get_valid_moves(self.board)

    # Remove piece(change it to an Empty piece)
    def remove(self, piece: Piece) -> None:
        if isinstance(piece, King):
            if piece.color == RED:
                self.red_kings = 0
            else:
                self.black_kings = 0
        self.board[piece.row][piece.col] = Empty(
            piece.row, piece.col, WHITE)
