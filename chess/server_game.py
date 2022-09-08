
# 3rd-party libraries
import pygame

# Custom imports
from .board import Board
from chess.constants import BLACK, BLUE, OFFSET, RED, SQUARE_SIZE
from chess.piece import Cannon, Elephant, Empty, Guard, Horse, King, Rook, Soldier


class ServerGame:
    def __init__(self) -> None:
        self._init()

    def _init(self) -> None:
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.full = False

    # Reset the board
    def reset(self) -> None:
        self._init()

    # Drawing the board
    def update(self, win: pygame.surface.Surface, player_color) -> None:
        self.board.draw(win)
        if player_color == self.turn:
            self.draw_valid_moves(self.valid_moves, win)
        pygame.display.update()

    # Select a piece
    def select(self, row: int, col: int) -> None:
        if self.selected:
            # If it is not a valid move
            if not self._move(row, col):
                self.valid_moves = {}   # Don't show the blue circles
            # Set selected to None no matter the move is valid or not TODO: Can do better
            self.selected = None

        else:
            piece = self.board.get_piece(row, col)
            if not isinstance(piece, Empty) and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)

    # Move a piece
    def _move(self, row: int, col: int) -> bool:
        # Target piece(piece that want to move to)
        piece = self.board.get_piece(row, col)
        if self.selected and (row, col) in self.valid_moves:    # Remove for debug use
            if isinstance(piece, (King, Rook, Horse, Cannon, Guard, Elephant, Soldier)) and piece.color != self.turn:
                self.board.remove(piece)
                self.board.move(self.selected, row, col)
                self.change_turn()
            elif isinstance(piece, Empty):
                self.board.move(self.selected, row, col)
                self.change_turn()
            else:
                return False
        else:
            return False

        return True

    # Change player turn
    def change_turn(self) -> None:
        self.valid_moves = {}
        self.turn = BLACK if self.turn == RED else RED

    # Draw valid moves(blue circles)
    def draw_valid_moves(self, moves, win: pygame.surface.Surface) -> None:
        for move in moves:
            row, col = move
            pygame.draw.circle(
                win, BLUE, (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET), 15)
