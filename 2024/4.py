class WordFinder:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            self._grid = [l.strip() for l in f]
        self._rows = len(self._grid)
        self._cols = len(self._grid[0])
        self._pattern = 'XMAS'
    
    def xmas_suffixes(self, x, y, i, dir):
        if x < 0 or x >= self._cols or y < 0 or y >= self._rows:
            return 0
        if i == len(self._pattern) - 1:
            return self._grid[y][x] == self._pattern[-1]
        if self._grid[y][x] != self._pattern[i]:
            return 0
        return self.xmas_suffixes(x + dir[0], y + dir[1], i + 1, dir)

    def number_of_patterns(self):
        total = 0
        for x in range(self._cols):
            for y in range(self._rows):
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        total += self.xmas_suffixes(x, y, 0, (dx, dy))
        return total        

    def has_cross(self, x, y):
        if self._grid[y][x] != 'A':
            return False
        m = 0
        s = 0
        for dx in (-1, 1):
            for dy in (-1, 1):
                if self._grid[y + dy][x + dx] == 'M':
                    m += 1
                if self._grid[y + dy][x + dx] == 'S':
                    s += 1
        if (m, s) != (2, 2):
            return False
        return self._grid[y + 1][x + 1] != self._grid[y - 1][x - 1]

    def number_of_crosses(self):
        crosses = 0
        for y in range(1, self._rows - 1):
            for x in range(1, self._cols - 1):
                if self.has_cross(x, y):
                    crosses += 1
        return crosses


def solve_first():
    word_finder = WordFinder()
    return word_finder.number_of_patterns()



def solve_second():
    word_finder = WordFinder()
    return word_finder.number_of_crosses()

        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()
