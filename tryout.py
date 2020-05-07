from pathlib import Path

from gol.board import Board, Size
from gol.view import Viewer

if __name__ == '__main__':
    viewer = Viewer()
    height, width = 10, 20
    board = Board(
        size = Size(height, width),
        # config_path = Path('seed.txt'),
        # output_dir = Path('output'),
    )
    viewer.show(board)
    input("Press Enter to continue.")
    for i in range(int(1e6)):
        board.tick()
        viewer.show(board)
        input("Press Enter to continue.")

