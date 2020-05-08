class Rule:
    def in_range(self, cell, num_alive):
        return num_alive in range(
            self.min_alive, 
            self.max_alive + 1,
        )

class Underpopulation(Rule):
    def __init__(self):
        self.min_alive = 0
        self.max_alive = 1 

    def applies(self, cell, num_alive):
        return all([
            cell.alive,
            self.in_range(cell, num_alive),
        ])

    def mutate(self, cell):
        cell.alive = False

class Survival(Rule):
    def __init__(self):
        self.min_alive = 2
        self.max_alive = 3

    def applies(self, cell, num_alive):
        return all([
            cell.alive,
            self.in_range(cell, num_alive),
        ])

    def mutate(self, cell):
        pass

class Overpopulation(Rule):
    def __init__(self):
        self.min_alive = 4
        self.max_alive = 8

    def applies(self, cell, num_alive):
        return all([
            cell.alive,
            self.in_range(cell, num_alive),
        ])

    def mutate(self, cell):
        cell.alive = False

class Reproduction(Rule):
    def __init__(self):
        self.min_alive = 3
        self.max_alive = 3

    def applies(self, cell, num_alive):
        return all([
            not cell.alive,
            self.in_range(cell, num_alive),
        ])

    def mutate(self, cell):
        cell.alive = True

class Rules:
    def __init__(self):
        self.rules = [
            Underpopulation(),
            Survival(),
            Overpopulation(),
            Reproduction(),
        ]

    def apply(self, cell):
        num_alive = self.get_num_alive_neighbors(cell)
        for rule in self.rules:
            if rule.applies(cell, num_alive):
                rule.mutate(cell)
                break

    def get_num_alive_neighbors(self, cell):
        neighbors = self.get_neighbors(cell)
        alive = self.get_alive(neighbors)
        num_alive = len(alive)
        return num_alive

    def get_alive(self, cells):
        alive = [
            cell for cell in cells
            if cell.alive
        ]
        return alive

    def get_neighbors(self, cell):
        neighbors = [
            cell.left,
            cell.top,
            cell.right,
            cell.bottom,
        ]
        if self.exists(cell.top):
            neighbors += [
                cell.top.left,
                cell.top.right,
            ]
        if self.exists(cell.bottom):
            neighbors += [
                cell.bottom.left,
                cell.bottom.right,
            ]
        neighbors = self.get_existing(neighbors)
        return neighbors

    def exists(self, cell):
        return cell is not None

    def get_existing(self, cells):
        existing = [
            cell for cell in cells 
            if self.exists(cell)
        ]
        return existing

