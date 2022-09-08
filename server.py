# Python built-in libraries
import logging
import os
import pickle
import socket
import threading

# 3rd-party libraries
from dotenv import load_dotenv

# Custom imports
from chess.constants import BLACK, RED
from chess.server_game import ServerGame

load_dotenv()

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Global Variable
game = ServerGame()
current_player = 0


def thread_client(client_socket: socket.socket, address, player_color):
    global current_player, game
    client_socket.sendall(pickle.dumps(
        {"player_color": player_color, "game": game}))
    while True:
        try:
            data = client_socket.recv(8192)
            if not data:
                break
            data = pickle.loads(data)
            print(f"Received from client {address}: {data}")
            if "get" in data:
                pass
            if "select" in data:
                row, col = data["select"]["row"], data["select"]["col"]
                game.select(row, col)

            print(f"Sending to client {address}: {game}")
            client_socket.sendall(pickle.dumps({"game": game}))
        except Exception as e:
            logging.error(e)
            break
    logging.info(f"Client disconnected. {address}")
    current_player -= 1
    client_socket.close()


def main():
    global current_player, game
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((os.getenv("HOST"), int(os.getenv("PORT"))))
        s.listen()
        logging.info("Server started.")

        while True:
            try:
                connection, address = s.accept()
                logging.info(f"Connected by {address}. Starting new thread.")

                current_player += 1
                if current_player % 2 == 1:
                    player_color = RED
                    logging.info("Creating a new game.")
                else:
                    player_color = BLACK
                    game.full = True
                    logging.info("2 players joined. Game start.")

                thread = threading.Thread(target=thread_client, args=(
                    connection, address, player_color))
                thread.start()
            except Exception as e:
                logging.error(e)
                break
        logging.info("Server stopped.")


if __name__ == "__main__":
    main()
