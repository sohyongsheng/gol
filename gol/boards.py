from gol.io import BoardIO
from gol.rules import Rules

class Board:
    def __init__(self, config_path, output_dir):
        self.config_path = config_path
        self.output_dir = output_dir
        self.io = BoardIO(output_dir)
        self.generation, self.cells = self.io.read(config_path)
        self.link(self.cells)
        self.rules = Rules()

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

