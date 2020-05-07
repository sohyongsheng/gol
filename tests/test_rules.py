from pathlib import Path

from gol.board import Board
from gol.cell import Cell
from gol.rules import (
    Underpopulation, 
    Overpopulation, 
    Reproduction, 
    Rules,
    Survival,
)
import pytest

class TestUnderpopulation():
    @pytest.fixture(scope = 'class')
    def underpopulation(self):
        return Underpopulation()

    def test_apply(self, underpopulation):
        # Cell should die during underpopulation.
        for num_alive in [0, 1]:
            cell = Cell(alive = True)
            underpopulation.apply(cell, num_alive)
            assert not cell.alive
        # No effect for alive cell when underpopulation 
        # doesn't apply.
        for num_alive in [2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = True)
            underpopulation.apply(cell, num_alive)
            assert cell.alive
        # No effect for dead cell.
        for num_alive in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = False)
            underpopulation.apply(cell, num_alive)
            assert not cell.alive

class TestSurvival():
    @pytest.fixture(scope = 'class')
    def survival(self):
        return Survival()

    def test_apply(self, survival):
        # Alive cell continues to live.
        for num_alive in [2, 3]:
            cell = Cell(alive = True)
            survival.apply(cell, num_alive)
            assert cell.alive
        # No effect when out of working range.
        for num_alive in [0, 1, 4, 5, 6, 7, 8]:
            cell = Cell(alive = True)
            survival.apply(cell, num_alive)
            assert cell.alive
        # No effect when cell is dead.
        for num_alive in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = False)
            survival.apply(cell, num_alive)
            assert not cell.alive

class TestOverpopulation():
    @pytest.fixture(scope = 'class')
    def overpopulation(self):
        return Overpopulation()

    def test_apply(self, overpopulation):
        # Cell should die during overpopulation.
        for num_alive in [4, 5, 6, 7, 8]:
            cell = Cell(alive = True)
            overpopulation.apply(cell, num_alive)
            assert not cell.alive
        # No effect when not in working range of overpopulation.
        for num_alive in [0, 1, 2, 3]:
            cell = Cell(alive = True)
            overpopulation.apply(cell, num_alive)
            assert cell.alive
        # No effect when cell is already dead.
        for num_alive in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = False)
            overpopulation.apply(cell, num_alive)
            assert not cell.alive

class TestReproduction():
    @pytest.fixture(scope = 'class')
    def reproduction(self):
        return Reproduction()

    def test_apply(self, reproduction):
        # Only reproduce when number of alive neighbors 
        # is exactly 3.
        num_alive = 3
        cell = Cell(alive = False)
        reproduction.apply(cell, num_alive)
        assert cell.alive
        # No effect for out of working range.
        for num_alive in [0, 1, 2, 4, 5, 6, 7, 8]:
            cell = Cell(alive = False)
            reproduction.apply(cell, num_alive)
            assert not cell.alive
        # No effect when cell is already alive.
        for num_alive in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            cell = Cell(alive = True)
            reproduction.apply(cell, num_alive)
            assert cell.alive

class TestRules():
    @pytest.fixture(scope = 'class')
    def rules(self):
        return Rules()

    @pytest.fixture(scope = 'class')
    def get_board(self):
        def _get_board(seed_name): 
            seed_dir = Path('tests', 'seeds')
            seed_path = seed_dir / seed_name
            board = Board(config_path = seed_path)
            return board
        return _get_board

    def test_get_num_alive_neighbors(self, rules, get_board):
        board = get_board('simple.txt')
        # First row.
        cell = board.cells[0][0]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 1
        cell = board.cells[0][1]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 2
        cell = board.cells[0][2]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 0
        # Second row.
        cell = board.cells[1][0]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 3
        cell = board.cells[1][1]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 5
        cell = board.cells[1][2]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 2
        # Third row.
        cell = board.cells[2][0]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 2
        cell = board.cells[2][1]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 3
        cell = board.cells[2][2]
        num_alive = rules.get_num_alive_neighbors(cell)
        assert num_alive == 1

    def test_apply(self, rules, get_board):
        # Dead cell, 0 alive neighbours.
        board = get_board('dead_0.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Dead cell, 1 alive neighbour.
        board = get_board('dead_1.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Dead cell, 2 alive neighbours.
        board = get_board('dead_2.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Dead cell, 3 alive neighbours.
        board = get_board('dead_3.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert center_cell.alive
        # Dead cell, 4 alive neighbours.
        board = get_board('dead_4.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Dead cell, 5 alive neighbours.
        board = get_board('dead_5.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Dead cell, 6 alive neighbours.
        board = get_board('dead_6.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Dead cell, 7 alive neighbours.
        board = get_board('dead_7.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Dead cell, 8 alive neighbours.
        board = get_board('dead_8.txt')
        center_cell = board.cells[1][1]
        assert not center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Alive cell, 0 alive neighbours.
        board = get_board('alive_0.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Alive cell, 1 alive neighbour.
        board = get_board('alive_1.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Alive cell, 2 alive neighbours.
        board = get_board('alive_2.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert center_cell.alive
        # Alive cell, 3 alive neighbours.
        board = get_board('alive_3.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert center_cell.alive
        # Alive cell, 4 alive neighbours.
        board = get_board('alive_4.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Alive cell, 5 alive neighbours.
        board = get_board('alive_5.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Alive cell, 6 alive neighbours.
        board = get_board('alive_6.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Alive cell, 7 alive neighbours.
        board = get_board('alive_7.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
        # Alive cell, 8 alive neighbours.
        board = get_board('alive_8.txt')
        center_cell = board.cells[1][1]
        assert center_cell.alive
        rules.apply(center_cell)
        assert not center_cell.alive
