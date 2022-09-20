# Python built-in libraries
import os
import pickle
import socket
from typing import Tuple

# 3rd-party libraries
from dotenv import load_dotenv
import pygame

# Custom imports
from chess.constants import HEIGHT, SQUARE_SIZE, WIDTH
from chess.server_game import ServerGame

load_dotenv()

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chinese Chess")


def get_row_col_from_mouse(pos: Tuple[int, int]):
    x, y = pos
    return min(y // SQUARE_SIZE, 9), min(x // SQUARE_SIZE, 8)


def send(socket: socket.socket, data: dict) -> dict:
    socket.sendall(pickle.dumps(data))
    total_data = []
    while True:
        data = socket.recv(8192)
        total_data.append(data)
        if len(b"".join(total_data)) > 3000:
            break

    return pickle.loads(b"".join(total_data))


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((os.getenv("HOST"), int(os.getenv("PORT"))))
        data = s.recv(8192)
        data = pickle.loads(data)
        player_color, game = data["player_color"], data["game"]

        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(FPS)

            data = send(s, {"get": ""})
            game: ServerGame = data["game"]

            if game.board.black_kings == 0 or game.board.red_kings == 0:
                run = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if game.full:
                        if player_color == game.turn:
                            row, col = get_row_col_from_mouse(
                                pygame.mouse.get_pos())
                            send(s, {"select": {"row": row, "col": col}})
                        else:
                            print("Not your turn yet.")
                    else:
                        print("Wait for the other player.")

            game.update(WIN, player_color)

        pygame.quit()


if __name__ == "__main__":
    main()
