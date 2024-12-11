from collections import defaultdict


class AntinodeFinder:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            self._grid = [l.strip() for l in f]
        self._rows = len(self._grid)
        self._cols = len(self._grid[0])
        self._antennas = defaultdict(list)
        for y in range(self._rows):
            for x in range(self._cols):
                if self._grid[y][x] != '.':
                    self._antennas[self._grid[y][x]].append((x, y))
    
    def is_valid_coordinate(self, x, y):
        return x >= 0 and x < self._cols and y >= 0 and y < self._rows
    
    def number_of_antinodes(self):
        antinodes = set()
        for antenna in self._antennas:
            coords = self._antennas[antenna]
            if len(coords) < 2:
                continue
            for i in range(len(coords)):
                x, y = coords[i]
                for j in range(i + 1, len(coords)):
                    x1, y1 = coords[j]
                    dx, dy = x1 - x, y1 - y
                    if self.is_valid_coordinate(x1 + dx, y1 + dy):
                        antinodes.add((x1 + dx, y1 + dy))
                    if self.is_valid_coordinate(x - dx, y - dy):
                        antinodes.add((x - dx, y - dy))
        return len(antinodes)
    
    def number_of_harmonic_antinodes(self):
        antinodes = set()
        for antenna in self._antennas:
            coords = self._antennas[antenna]
            if len(coords) < 2:
                continue
            for i in range(len(coords)):
                x0, y0 = coords[i]
                for j in range(i + 1, len(coords)):
                    x, y = x0, y0
                    x1, y1 = coords[j]
                    dx, dy = x1 - x, y1 - y

                    while self.is_valid_coordinate(x, y):
                        antinodes.add((x, y))
                        x -= dx
                        y -= dy
                    while self.is_valid_coordinate(x1, y1):
                        antinodes.add((x1, y1))
                        x1 += dx
                        y1 += dy
        return len(antinodes)


        
    

def solve_first():
    antinode_finder = AntinodeFinder()
    return antinode_finder.number_of_antinodes()

def solve_second():
    antinode_finder = AntinodeFinder()
    return antinode_finder.number_of_harmonic_antinodes()


        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()
