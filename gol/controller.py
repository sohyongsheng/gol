import curses
import time

class Controller:
    def __init__(self, view, board, time_delay):
        self.view = view
        self.board = board
        self.time_delay = time_delay

    def generate_boards(self):
        yield self.board
        while True:
            time.sleep(self.time_delay)
            self.board.tick()
            yield self.board

    def play(self):
        curses.wrapper(self.view.play, self.generate_boards)
