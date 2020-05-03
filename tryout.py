from pathlib import Path

from gol.boards import Board
from gol.view import Viewer

if __name__ == '__main__':
    viewer = Viewer()
    seed_path = Path('seed.txt')
    output_dir = Path('output')
    board = Board(seed_path, output_dir)
    viewer.show(board)
    while True:
        board.tick()
        viewer.show(board)

