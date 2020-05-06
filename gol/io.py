from gol.cells import Cell

class BoardIO:
    def __init__(self, output_dir = None):
        self.symbols = {
            'alive': '1',
            'dead': '0',
        }
        self.output_dir = output_dir
        self.reader = Reader(self.symbols)

    def read(self, config_path):
        generation, cells =  self.reader.read(config_path)
        return generation, cells

class Reader:
    def __init__(self, symbols):
        self.symbols = symbols

    def read(self, config_path):
        generation = self.get_generation(config_path)
        cells = self.get_cells(config_path)
        return generation, cells

    def get_generation(self, config_path):
        s = str(config_path.stem)
        if s.startswith('gen_'):
            _, generation = s.split('_')
            generation = int(generation)
        else:
            generation = 0
        return generation

    def get_cells(self, config_path):
        with config_path.open() as f:
            lines = (line.strip() for line in f)
            lines = (line for line in lines if line)
            cells = [self.get_row(line) for line in lines]
        return cells

    def get_cell(self, c):
        assert c in self.symbols.values()
        alive = (c == self.symbols['alive'])
        cell = Cell(alive = alive)
        return cell

    def get_row(self, line):
        row = [self.get_cell(c) for c in line]
        return row
