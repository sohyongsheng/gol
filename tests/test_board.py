from pathlib import Path

from gol.board import Board
import pytest

class TestBoard():
    @pytest.fixture(scope = 'class')
    def board(self):
        test_dir = Path('tests')
        seed_path = test_dir / 'seeds' / 'simple.txt'
        board = Board(config_path = seed_path)
        return board
        
    def test_init(self, board):
        cells = board.cells
        # Start from top left hand corner.
        start = cells[0][0]
        # Move towards bottom right hand corner.
        end = cells[-1][-1]
        assert start is not end
        # Confirm some neighbor cells don't exist.
        assert start.left is None
        assert start.top is None
        assert end.right is None
        assert end.bottom is None
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

