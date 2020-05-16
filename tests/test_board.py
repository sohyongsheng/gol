from pathlib import Path

import pytest

from gol.board import Board

class TestBoard():
    @pytest.fixture(scope = 'class')
    def get_board(self):
        def wrapper(wrap_around = False):
            test_dir = Path('tests')
            seed_path = test_dir / 'seeds' / 'simple.txt'
            board = Board(
                config_path = seed_path,
                wrap_around = wrap_around,
            )
            return board
        return wrapper
        
    def test_init(self, get_board):
        board = get_board()
        cells = board.cells
        # Start from top left hand corner.
        start = cells[0][0]
        # Target is bottom right hand corner.
        end = cells[-1][-1]
        assert start is not end

        # Confirm some neighbor cells don't exist.
        assert start.left is None
        assert start.top is None
        assert end.right is None
        assert end.bottom is None

        # Move towards end point.
        cell = (
            start.right.right
            .bottom.left.left
            .bottom.right.right
        )
        assert cell is end
        # Move back to start point again.
        cell = (
            cell.top.top
            .left.bottom.bottom
            .left.top.top
        )
        assert cell is start

        # Board with wrap-around.
        board = get_board(wrap_around = True)
        cells = board.cells
        # Start from top left hand corner.
        top_left = cells[0][0]
        top_right = cells[0][-1]
        bottom_left = cells[-1][0]
        bottom_right = cells[-1][-1]
        assert top_left.left is top_right
        assert top_right.top is bottom_right
        assert bottom_right.right is bottom_left
        assert bottom_left.bottom is top_left
