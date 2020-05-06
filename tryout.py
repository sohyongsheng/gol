from pathlib import Path

from gol.boards import Board
from gol.view import Viewer

if __name__ == '__main__':
    viewer = Viewer()
    board = Board(
        size = (80, 24),
        # config_path = Path('seed.txt'),
        # output_dir = Path('output'),
    )
    viewer.show(board)
    for i in range(int(1e6)):
        board.tick()
        viewer.show(board)

