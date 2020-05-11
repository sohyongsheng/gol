import curses
import time

class View:
    def __init__(self):
        self.symbols = {
            'alive': '\N{WHITE LARGE SQUARE}',
            'dead': '\N{BLACK LARGE SQUARE}',
        }

    def play(self, stdscr, generate_boards):
        curses.use_default_colors()
        visibility = 0
        curses.curs_set(visibility)
        for board in generate_boards():
            stdscr.erase()
            s = self.stringify_view(board)
            stdscr.addstr(s)
            stdscr.refresh()

    def stringify_view(self, board):
        status = f"Generation: {board.generation}"
        s = '\n'.join([
            status, 
            self.stringify_board(board),
        ])
        return s

    def stringify_cell(self, cell):
        k = 'alive' if cell.alive else 'dead'
        c = self.symbols[k]
        return c

    def stringify_row(self, row):
        s = ''.join(
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

