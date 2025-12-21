class PaperRolls:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            self.grid = [[c for c in line.strip()] for line in f]

            self.y0 = len(self.grid)
            self.x0 = len(self.grid[0])
        self.num_removed = 0

    def coordinates_are_valid(self, y, x):
        return (0 <= y < self.y0) and (0 <= x < self.x0)
    
    def build_adjacency_counts(self):
        num_adjacent = [[0] * self.x0 for _ in range(self.y0)]
        for y in range(self.y0):
            for x in range(self.x0):
                if self.grid[y][x] != '@':
                    continue
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dy == dx == 0:
                            continue
                        if not self.coordinates_are_valid(y + dy, x + dx):
                            continue
                        num_adjacent[y + dy][x + dx] += 1
                        
        return num_adjacent

    def solve_first(self):
        num_adjacent = self.build_adjacency_counts()
        
        return sum(
            [1 if (num_adjacent[y][x] < 4) and (self.grid[y][x] == '@') else 0
            for y in range(self.y0)
            for x in range(self.x0)]
        )
    
    def remove_accessible_rolls(self, y, x, num_adjacent):
        if not self.coordinates_are_valid(y, x):
            return
        if self.grid[y][x] != '@':
            return
        if num_adjacent[y][x] >= 4:
            return
        self.grid[y][x] = '.'
        self.num_removed += 1
        neighbor_rolls = []
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == dx == 0:
                    continue
                if not self.coordinates_are_valid(y + dy, x + dx):
                    continue
                if self.grid[y + dy][x + dx] == '@':
                    num_adjacent[y + dy][x + dx] -= 1
                    neighbor_rolls.append((y, x))
        for nr in neighbor_rolls:
            self.remove_accessible_rolls(nr[0], nr[1], num_adjacent)

    def solve_second(self):
        num_adjacent = self.build_adjacency_counts()
        self.num_removed = 0
        while True:
            prev_num_removed = self.num_removed
            for y in range(self.y0):
                for x in range(self.x0):
                    self.remove_accessible_rolls(y, x, num_adjacent)
            if prev_num_removed == self.num_removed:
                return self.num_removed


def main():
    paper_rolls = PaperRolls()
    print(paper_rolls.solve_second())

if __name__ == '__main__':
    main()
