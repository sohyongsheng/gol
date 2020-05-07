from pathlib import Path
import unittest

from gol.board import Board
from gol.cell import Cell
from gol.rules import (
    Underpopulation, 
    Overpopulation, 
    Reproduction, 
    Rules,
    Survival,
)

class TestUnderpopulation(unittest.TestCase):
    def setUp(self):
        self.underpopulation = Underpopulation()

    def test_apply(self):
        # Cell should die during underpopulation.
        for num_alive in [0, 1]:
            cell = Cell(alive = True)
            self.underpopulation.apply(cell, num_alive)
            self.assertTrue(not cell.alive)
        # No effect for alive cell when underpopulation 
        # doesn't apply.
        for num_alive in [2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = True)
            self.underpopulation.apply(cell, num_alive)
            self.assertTrue(cell.alive)
        # No effect for dead cell.
        for num_alive in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = False)
            self.underpopulation.apply(cell, num_alive)
            self.assertTrue(not cell.alive)

class TestSurvival(unittest.TestCase):
    def setUp(self):
        self.survival = Survival()

    def test_apply(self):
        # Alive cell continues to live.
        for num_alive in [2, 3]:
            cell = Cell(alive = True)
            self.survival.apply(cell, num_alive)
            self.assertTrue(cell.alive)
        # No effect when out of working range.
        for num_alive in [0, 1, 4, 5, 6, 7, 8]:
            cell = Cell(alive = True)
            self.survival.apply(cell, num_alive)
            self.assertTrue(cell.alive)
        # No effect when cell is dead.
        for num_alive in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = False)
            self.survival.apply(cell, num_alive)
            self.assertTrue(not cell.alive)

class TestOverpopulation(unittest.TestCase):
    def setUp(self):
        self.overpopulation = Overpopulation()

    def test_apply(self):
        # Cell should die during overpopulation.
        for num_alive in [4, 5, 6, 7, 8]:
            cell = Cell(alive = True)
            self.overpopulation.apply(cell, num_alive)
            self.assertTrue(not cell.alive)
        # No effect when not in working range of overpopulation.
        for num_alive in [0, 1, 2, 3]:
            cell = Cell(alive = True)
            self.overpopulation.apply(cell, num_alive)
            self.assertTrue(cell.alive)
        # No effect when cell is already dead.
        for num_alive in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = False)
            self.overpopulation.apply(cell, num_alive)
            self.assertTrue(not cell.alive)

class TestReproduction(unittest.TestCase):
    def setUp(self):
        self.reproduction = Reproduction()

    def test_apply(self):
        # Only reproduce when number of alive neighbors 
        # is exactly 3.
        num_alive = 3
        cell = Cell(alive = False)
        self.reproduction.apply(cell, num_alive)
        self.assertTrue(cell.alive)
        # No effect for out of working range.
        for num_alive in [0, 1, 2, 4, 5, 6, 7, 8]:
            cell = Cell(alive = False)
            self.reproduction.apply(cell, num_alive)
            self.assertTrue(not cell.alive)
        # No effect when cell is already alive.
        for num_alive in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = True)
            self.reproduction.apply(cell, num_alive)
            self.assertTrue(cell.alive)

class TestRules(unittest.TestCase):
    def setUp(self):
        self.seed_dir = Path('tests', 'seeds')
        self.rules = Rules()

    def test_get_num_alive_neighbors(self):
        seed_path = self.seed_dir / 'simple.txt'
        board = Board(config_path = seed_path)
        # First row.
        cell = board.cells[0][0]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 1)
        cell = board.cells[0][1]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 2)
        cell = board.cells[0][2]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 0)
        # Second row.
        cell = board.cells[1][0]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 3)
        cell = board.cells[1][1]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 5)
        cell = board.cells[1][2]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 2)
        # Third row.
        cell = board.cells[2][0]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 2)
        cell = board.cells[2][1]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 3)
        cell = board.cells[2][2]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 1)

    def test_apply(self):
        # Dead cell, 0 alive neighbours.
        seed_path = self.seed_dir / 'dead_0.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Dead cell, 1 alive neighbour.
        seed_path = self.seed_dir / 'dead_1.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Dead cell, 2 alive neighbours.
        seed_path = self.seed_dir / 'dead_2.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Dead cell, 3 alive neighbours.
        seed_path = self.seed_dir / 'dead_3.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertTrue(center_cell.alive)
        # Dead cell, 4 alive neighbours.
        seed_path = self.seed_dir / 'dead_4.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Dead cell, 5 alive neighbours.
        seed_path = self.seed_dir / 'dead_5.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Dead cell, 6 alive neighbours.
        seed_path = self.seed_dir / 'dead_6.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Dead cell, 7 alive neighbours.
        seed_path = self.seed_dir / 'dead_7.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Dead cell, 8 alive neighbours.
        seed_path = self.seed_dir / 'dead_8.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertFalse(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Alive cell, 0 alive neighbours.
        seed_path = self.seed_dir / 'alive_0.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Alive cell, 1 alive neighbour.
        seed_path = self.seed_dir / 'alive_1.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Alive cell, 2 alive neighbours.
        seed_path = self.seed_dir / 'alive_2.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertTrue(center_cell.alive)
        # Alive cell, 3 alive neighbours.
        seed_path = self.seed_dir / 'alive_3.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertTrue(center_cell.alive)
        # Alive cell, 4 alive neighbours.
        seed_path = self.seed_dir / 'alive_4.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Alive cell, 5 alive neighbours.
        seed_path = self.seed_dir / 'alive_5.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Alive cell, 6 alive neighbours.
        seed_path = self.seed_dir / 'alive_6.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Alive cell, 7 alive neighbours.
        seed_path = self.seed_dir / 'alive_7.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
        # Alive cell, 8 alive neighbours.
        seed_path = self.seed_dir / 'alive_8.txt'
        board = Board(config_path = seed_path)
        center_cell = board.cells[1][1]
        self.assertTrue(center_cell.alive)
        self.rules.apply(center_cell)
        self.assertFalse(center_cell.alive)
