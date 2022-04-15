# Python built-in libraries
from typing import Tuple

# 3rd-party libraries
import pygame

# Custom imports
from chess.constants import HEIGHT, SQUARE_SIZE, WIDTH
from chess.game import Game


# Constants
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chinese Chess")


def get_row_col_from_mouse(pos: Tuple[int, int]):
    x, y = pos
    return y // SQUARE_SIZE, x // SQUARE_SIZE


def main() -> None:
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_row_col_from_mouse(pygame.mouse.get_pos())
                game.select(row, col)

        game.update()

        if game.board.black_kings == 0 or game.board.red_kings == 0:
            run = False

    pygame.quit()


if __name__ == "__main__":
    main()
