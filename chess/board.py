
# 3rd-party libraries
import pygame

# Custom imports
from chess.piece import Cannon, Elephant, Guard, Horse, King, Rook, Soldier
from .constants import BLACK, COLS, HEIGHT, OFFSET, ROWS, SQUARE_SIZE, WIDTH, YELLOW_ORANGE


class Board:
    def __init__(self) -> None:
        self.board: list = []
        self.selected_piece = None
        self.red_left = self.black_left = 16
        self.red_kings = self.black_kings = 0
        self.create_board()

    # Draw backgroun lines
    def draw_squares(self, win: pygame.Surface) -> None:
        # Fill background color
        win.fill(YELLOW_ORANGE)
        # Rows line
        for row in range(ROWS):
            pygame.draw.line(win, BLACK, (OFFSET, row * SQUARE_SIZE + OFFSET),
                             (WIDTH - OFFSET, row * SQUARE_SIZE + OFFSET), 2)
        # Cols line
        for col in range(COLS):
            pygame.draw.line(win, BLACK, (col * SQUARE_SIZE + OFFSET, OFFSET),
                             (col * SQUARE_SIZE + OFFSET, HEIGHT - OFFSET), 2)
        # Cross line
        pygame.draw.line(win, BLACK, (350, 50), (550, 250), 2)
        pygame.draw.line(win, BLACK, (550, 50), (350, 250), 2)
        pygame.draw.line(win, BLACK, (350, 750), (550, 950), 2)
        pygame.draw.line(win, BLACK, (550, 750), (350, 950), 2)
        # Remove middle line
        for col in range(1, COLS - 1):
            pygame.draw.line(win, YELLOW_ORANGE, (col * SQUARE_SIZE + OFFSET, 450),
                             (col * SQUARE_SIZE + OFFSET, 450 + SQUARE_SIZE), 2)

    # Add Pieces to the board
    def create_board(self) -> None:
        self.board.append([Rook(0, 0, "b"), Horse(0, 1, "b"), Elephant(0, 2, "b"), Guard(0, 3, "b"), King(
            0, 4, "b"), Guard(0, 5, "b"), Elephant(0, 6, "b"), Horse(0, 7, "b"), Rook(0, 8, "b")])
        self.board.append(["", "", "", "", "", "", "", "", ""])
        self.board.append(["", Cannon(2, 1, "b"), "", "",
                          "", "", "", Cannon(2, 7, "b"), ""])
        self.board.append([Soldier(3, 0, "b"), "", Soldier(3, 2, "b"), "", Soldier(
            3, 4, "b"), "", Soldier(3, 6, "b"), "", Soldier(3, 8, "b")])
        self.board.append(["", "", "", "", "", "", "", "", ""])
        self.board.append(["", "", "", "", "", "", "", "", ""])
        self.board.append([Soldier(6, 0, "r"), "", Soldier(6, 2, "r"), "", Soldier(
            6, 4, "r"), "", Soldier(6, 6, "r"), "", Soldier(6, 8, "r")])
        self.board.append(["", Cannon(7, 1, "r"), "", "",
                          "", "", "", Cannon(7, 7, "r"), ""])
        self.board.append(["", "", "", "", "", "", "", "", ""])
        self.board.append([Rook(9, 0, "r"), Horse(9, 1, "r"), Elephant(9, 2, "r"), Guard(9, 3, "r"), King(
            9, 4, "r"), Guard(9, 5, "r"), Elephant(9, 6, "r"), Horse(9, 7, "r"), Rook(9, 8, "r")])

    # Draw the board
    def draw(self, win: pygame.Surface) -> None:
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != "":
                    self.board[row][col].draw(win)
