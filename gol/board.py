from gol.generator import RandomCellGenerator
from gol.io import BoardIO
from gol.misc import time_elapsed
from gol.rules import Rules

class Size:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        s = "height, width = {self.height}, {self.width}"
        return s

class Board:
    def __init__(self, 
        size = None,
        config_path = None, 
        wrap_around = False,
        output_dir = None,
    ):
        self.io = BoardIO(output_dir = output_dir)
        if config_path is not None:
            assert size is None
            self.config_path = config_path
            self.generation, self.cells = self.io.read(config_path)
            self.size = self.get_size(self.cells)
        else:
            assert size is not None
            self.generation = 0
            self.size = size
            self.generator = RandomCellGenerator()
            self.cells = self.generator.get_cells(self.size)
            s = self.get_size(self.cells)
        self.link(self.cells, wrap_around)
        self.rules = Rules()

    def get_size(self, cells):
        height = len(cells)
        row, *_ = cells
        width = len(row)
        size = Size(height, width)
        return size

    def link(self, cells, wrap_around):
        *tops, last = first, *bottoms = cells
        for top, bottom in zip(tops, bottoms):
            self.link_horizontally(top, wrap_around)
            self.link_vertically(top, bottom)
        self.link_horizontally(bottom, wrap_around)
        if wrap_around:
            self.link_vertically(last, first)

    def link_vertically(self, tops, bottoms):
        for top, bottom in zip(tops, bottoms):
            top.bottom, bottom.top = bottom, top

    def link_horizontally(self, row, wrap_around):
        *lefts, last = first, *rights = row
        for left, right in zip(lefts, rights):
            left.right, right.left = right, left
        if wrap_around:
            last.right, first.left = first, last

    # @time_elapsed
    def tick(self):
        self.generation += 1
        for row in self.cells:
            for cell in row:
                self.rules.apply(cell)
        for row in self.cells:
            for cell in row:
                cell.update()

