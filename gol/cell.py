class Cell:
    def __init__(self, alive = False):
        self.alive = alive
        self.to_live = None
        self.left = None
        self.top = None
        self.right = None
        self.bottom = None

    def update(self):
        if self.to_live is not None:
            self.alive = self.to_live
            self.to_live = None

