from pathlib import Path

from gol.board import Board, Size
from gol.controller import Controller
from gol.view import View

if __name__ == '__main__':
    view = View()
    seed_dir = Path('seeds')
    board = Board(
        # size = Size(20, 20),
        config_path = seed_dir / 'glider.txt',
        # output_dir = Path('output'),
    )
    controller = Controller(view, board)
    controller.play()
