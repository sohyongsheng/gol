from pathlib import Path
import unittest

from gol.boards import Board
from gol.cells import Cell
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
        test_dir = Path('tests')
        seed_path = test_dir / 'seeds' / 'simple.txt'
        output_dir = Path('output')
        self.board = Board(seed_path, output_dir)
        self.rules = Rules()

    def test_get_num_alive_neighbors(self):
        # First row.
        cell = self.board.cells[0][0]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 1)
        cell = self.board.cells[0][1]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 2)
        cell = self.board.cells[0][2]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 0)
        # Second row.
        cell = self.board.cells[1][0]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 3)
        cell = self.board.cells[1][1]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 5)
        cell = self.board.cells[1][2]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 2)
        # Third row.
        cell = self.board.cells[2][0]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 2)
        cell = self.board.cells[2][1]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 3)
        cell = self.board.cells[2][2]
        num_alive = self.rules.get_num_alive_neighbors(cell)
        self.assertEqual(num_alive, 1)

