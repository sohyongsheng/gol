from gol.generator import RandomCellGenerator
from gol.io import BoardIO
from gol.rules import Rules

class Size:
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Board:
    def __init__(self, 
        size = None,
        config_path = None, 
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
            self.size = size
            self.generator = RandomCellGenerator()
            self.cells = self.generator.get_cells(self.size)
        self.link(self.cells)
        self.rules = Rules()

    def get_size(self, cells):
        height = len(cells)
        row, *_ = cells
        width = len(row)
        size = Size(height, width)
        return size

    def link(self, cells):
        *tops, _ = _, *bottoms = cells
        for top, bottom in zip(tops, bottoms):
            self.link_horizontally(top)
            self.link_vertically(top, bottom)
        self.link_horizontally(bottom)

    def link_vertically(self, tops, bottoms):
        for top, bottom in zip(tops, bottoms):
            top.bottom, bottom.top = bottom, top

    def link_horizontally(self, row):
        *lefts, _ = _, *rights = row
        for left, right in zip(lefts, rights):
            left.right, right.left = right, left

    def tick(self):
        for row in self.cells:
            for cell in row:
                self.rules.apply(cell)

