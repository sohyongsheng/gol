from pathlib import Path

from gol.boards import Board, Size
from gol.view import Viewer

if __name__ == '__main__':
    viewer = Viewer()
    height, width = 24, 80
    board = Board(
        size = Size(height, width),
        # config_path = Path('seed.txt'),
        # output_dir = Path('output'),
    )
    viewer.show(board)
    for i in range(int(1e6)):
        board.tick()
        viewer.show(board)

