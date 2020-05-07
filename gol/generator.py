import random

from gol.cell import Cell

class BooleanDice:
    def __init__(self, probability = 0.5):
        self.probability = probability

    def roll(self):
        return random.random() > self.probability

class RandomCellGenerator:
    def __init__(self, frac_alive = 0.5):
        self.dice = BooleanDice(frac_alive)

    def get_cells(self, size):
        cells = [
            self.get_row(size.width)
            for i in range(size.height)
        ]
        return cells

    def get_row(self, width):
        row = [
            Cell(alive = self.dice.roll())
            for j in range(width)
        ]
        return row
