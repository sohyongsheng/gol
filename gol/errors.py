import textwrap

class Error(Exception):
    def prefix(self, message):
        s = f"Error: {self.message}"
        s = textwrap.fill(s)
        return s

class BadInitialization(Error):
    def __init__(self, message, seed_path, size):
        self.message = message
        self.seed_path = seed_path
        self.size = size

    def __str__(self):
        s = '\n'.join([
            self.prefix(self.message),
            f"Seed path: {self.seed_path}",
            f"Height, width: {self.size}",
        ])
        return s

class SeedPathNotFound(Error):
    def __init__(self, message, seed_path):
        self.message = message
        self.seed_path = seed_path

    def __str__(self):
        s = '\n'.join([
            self.prefix(self.message),
            f"Seed path: {self.seed_path}",
        ])
        return s

class BoardTooLarge(Error):
    def __init__(self, message, board_size, max_size):
        self.message = message
        self.board_size = board_size
        self.max_size = max_size

    def __str__(self):
        s = '\n'.join([
            self.prefix(self.message), (
                f"Board height, width: "
                f"{self.board_size.height}, "
                f"{self.board_size.width}"
            ), (
                f"Max height, width: "
                f"{self.max_size.height}, "
                f"{self.max_size.width}"
            ),
        ])
        return s

class InvalidSymbol(Error):
    def __init__(self, message, symbol):
        self.message = message
        self.symbol = symbol

    def __str__(self):
        s = '\n'.join([
            self.prefix(self.message),
            f"Invalid symbol: {self.symbol}",
        ])
        return s

class InconsistentWidths(Error):
    def __init__(self, message, unique_widths):
        self.message = message
        self.unique_widths = unique_widths

    def __str__(self):
        s = '\n'.join([
            self.prefix(self.message),
            f"Unique widths: {self.unique_widths}",
        ])
        return s

