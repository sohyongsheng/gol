import curses
import time

class Controller:
    def __init__(self, view, board):
        self.view = view
        self.board = board

    def generate_boards(self):
        yield self.board
        while True:
            time.sleep(0.3)
            self.board.tick()
            yield self.board

    def play(self):
        curses.wrapper(self.view.play, self.generate_boards)
