from gol.board import Board
from gol.controller import Controller
from gol.errors import Error
from gol.view import View
from gol.parse import Parser

if __name__ == '__main__':
    try:
        parser = Parser()
        args = parser.parse()
        view = View()
        board = Board(
            size = args.size,
            config_path = args.seed_path,
            wrap_around = args.wrap_around,
        )
        controller = Controller(view, board, args.time_delay)
        controller.play()
    except Error as error:
        print(error)
