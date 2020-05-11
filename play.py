from gol.board import Board
from gol.controller import Controller
from gol.view import View
from gol.parse import Parser

if __name__ == '__main__':
    parser = Parser()
    args = parser.parse()
    view = View()
    board = Board(
        size = args.size,
        config_path = args.seed_path,
    )
    controller = Controller(view, board, args.time_delay)
    controller.play()
