from pathlib import Path
import unittest

from gol.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        test_dir = Path('tests')
        seed_path = test_dir / 'seeds' / 'simple.txt'
        self.board = Board(config_path = seed_path)
        
    def test_init(self):
        cells = self.board.cells
        # Start from top left hand corner.
        start = cells[0][0]
        # Move towards bottom right hand corner.
        end = cells[-1][-1]
        self.assertIsNot(start, end)
        # Confirm some neighbor cells don't exist.
        self.assertIsNone(start.left)
        self.assertIsNone(start.top)
        self.assertIsNone(end.right)
        self.assertIsNone(end.bottom)
        cell = (
            start.right.right
            .bottom.left.left
            .bottom.right.right
        )
        self.assertIs(cell, end)
        # Move back to start point again.
        cell = (
            cell.top.top
            .left.bottom.bottom
            .left.top.top
        )
        self.assertIs(cell, start)

if __name__ == '__main__':
    unittest.main()
