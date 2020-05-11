from argparse import ArgumentParser
from pathlib import Path

from gol.board import Size

class Arguments:
    def __init__(self):
        self.seed_path = None
        self.size = None

class Parser:
    def __init__(self):
        self.parser = ArgumentParser(
            description = "Conway's Game of Life.",
        )
        self.parser.add_argument(
            '-p', '--seed_path',
            type = Path,
            help = "Path of seed text file."
        )
        self.parser.add_argument(
            '-s', '--size',
            nargs = 2,
            type = int,
            help = "Height and width of board.",
        )
        self.parser.add_argument(
            '-t', '--time_delay',
            type = float,
            default = 0.3,
            help = "Time delay before showing next generation.",
        )
        self.args = Arguments()

    def parse_size(self, size):
        height, width = size
        size = Size(height, width)
        return size

    def parse(self):
        args = self.parser.parse_args()
        self.args.time_delay = args.time_delay
        # TODO Throw and handle exceptions 
        # instead of abusing assertions.
        if args.seed_path is None:
            assert args.size is not None
            self.args.size = self.parse_size(args.size)
        else:
            assert args.size is None
            assert args.seed_path.is_file()
            self.args.seed_path = args.seed_path
        return self.args

