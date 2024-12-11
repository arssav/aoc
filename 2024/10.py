from collections import defaultdict

class TrailMap:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            self._grid = [list(map(int, l.strip())) for l in f]
        self._ratings = {}
        self._rows = len(self._grid)
        self._cols = len(self._grid[0])
        self._reachable_peaks = defaultdict(set)

    def is_valid_coordinate(self, x, y):
        return x >= 0 and x < self._cols and y >= 0 and y < self._rows
    
    def neighbors(self, x, y):
        yield (x + 1, y)
        yield (x - 1, y)
        yield (x, y + 1)
        yield (x, y - 1)

    def rating(self, x, y):
        if (x, y) in self._ratings:
            return self._ratings[(x, y)]
        if not self.is_valid_coordinate(x, y):
            return 0
        if self._grid[y][x] == 9:
            return 1

        rating = 0
        for (x1, y1) in self.neighbors(x, y):
            if self.is_valid_coordinate(x1, y1) and self._grid[y1][x1] == self._grid[y][x] + 1:
                rating += self.rating(x1, y1)
        self._ratings[(x, y)] = rating
        return rating


    def reachable_peaks(self, x, y):
        if (x, y) in self._reachable_peaks:
            return self._reachable_peaks[(x, y)]
        if not self.is_valid_coordinate(x, y):
            return set()
        if self._grid[y][x] == 9:
            return set([(x, y)])

        reachable = set()

        for (x1, y1) in self.neighbors(x, y):
            if self.is_valid_coordinate(x1, y1) and self._grid[y1][x1] == self._grid[y][x] + 1:
                reachable |= self.reachable_peaks(x1, y1)
    
        self._reachable_peaks[(x, y)] = reachable
        return reachable

    def trail_heads_score(self):
        total = 0
        for y in range(self._rows):
            for x in range(self._cols):
                if self._grid[y][x] == 0:
                    total += len(self.reachable_peaks(x, y))
        return total
    
    def trail_heads_rating(self):
        total = 0
        for y in range(self._rows):
            for x in range(self._cols):
                if self._grid[y][x] == 0:
                    total += self.rating(x, y)
        return total




def solve_first():
    trail_map = TrailMap()
    return trail_map.trail_heads_score()

def solve_second():
    trail_map = TrailMap()
    return trail_map.trail_heads_rating()



        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()
