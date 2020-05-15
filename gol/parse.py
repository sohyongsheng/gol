from argparse import ArgumentParser
from pathlib import Path

from gol.board import Size
from gol.errors import (
    BadInitialization, 
    SeedPathNotFound,
)

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
            help = (
                "Path of seed text file. "
                "If this is not specified, "
                "then we will initialize the board randomly. "
                "In that case, we must specify the size of "
                "the board. That said, we cannot specify "
                "both the seed path and size, nor can we "
                "leave both the seed path and size unspecified."
            ),
        )
        self.parser.add_argument(
            '-s', '--size',
            nargs = 2,
            type = int,
            help = (
                "Height and width of board. "
                "When this is specified, the board will be "
                "randomly initialized with each cell having an "
                "equal chance of being alive or dead. "
                "Also, we cannot specify the seed path "
                "if we specify the size of the board here."
            ),
        )
        self.parser.add_argument(
            '-t', '--time_delay',
            type = float,
            default = 0.3,
            help = (
                "Time delay between generations. "
                "More precisely, it's the time delay between "
                "drawing boards of consecutive generations."
            ),
        )
        self.args = Arguments()

    def parse(self):
        args = self.parser.parse_args()
        self.args.time_delay = args.time_delay
        if not (
            (args.seed_path is None and args.size is not None)
            or (args.seed_path is not None and args.size is None)
        ):
            raise BadInitialization((
                "Only either seed path or size must be given. "
                "We cannot specify both the seed path and size, "
                "nor can we leave both the seed path and size "
                "blank."
            ), args.seed_path, args.size)
        if args.seed_path is None:
            self.args.size = self.parse_size(args.size)
        else:
            if not args.seed_path.is_file():
                raise SeedPathNotFound(
                    "Seed path is not found.",
                    args.seed_path,
                )
            self.args.seed_path = args.seed_path
        return self.args

    def parse_size(self, size):
        height, width = size
        size = Size(height, width)
        return size

