class Viewer:
    def __init__(self):
        self.symbols = {
            'alive': 'X',
            'dead': '.',
        }

    def stringify_cell(self, cell):
        k = 'alive' if cell.alive else 'dead'
        c = self.symbols[k]
        return c

    def stringify_row(self, row):
        s = ' '.join(
            self.stringify_cell(cell)
            for cell in row
        )
        return s

    def stringify_board(self, board):
        s = '\n'.join(
            self.stringify_row(row) 
            for row in board.cells
        )
        return s

    def show(self, board):
        print(self.stringify_board(board))
        s = input("Press Enter to continue, or 'q' to exit.")
        if s == 'q':
            raise SystemExit

