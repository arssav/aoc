class LabMap:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            self._grid = [list(l.strip()) for l in f]
        self._rows = len(self._grid)
        self._cols = len(self._grid[0])
        for y in range(self._rows):
            for x in range(self._rows):
                if self._grid[y][x] == '^':
                    self._guard = (x, y)
                    break
        self._dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    def is_valid_pos(self, x, y):
        return x >= 0 and x < self._cols and y >= 0 and y < self._rows

    def guard_route(self):
        x, y = self._guard
        dir_index = 0
        route = set()
        while self.is_valid_pos(x, y):
            route.add((x, y))
            dx, dy = self._dirs[dir_index]
            if not self.is_valid_pos(x + dx, y + dy):
                break
            if self._grid[y + dy][x + dx] != '#':
                x += dx
                y += dy
                continue
            dir_index = (dir_index + 1) % len(self._dirs)
        return len(route)
    
    def is_looped(self):
        x, y = self._guard
        dir_index = 0
        route = set()
        while self.is_valid_pos(x, y):
            dx, dy = self._dirs[dir_index]
            if (x, y, dx, dy) in route:
                return True
            route.add((x, y, dx, dy))
            
            if not self.is_valid_pos(x + dx, y + dy):
                break
            if self._grid[y + dy][x + dx] != '#':
                x += dx
                y += dy
                continue
            dir_index = (dir_index + 1) % len(self._dirs)
        return False

    def possible_obstructions(self):
        obstructions = 0
        for y in range(self._rows):
            print(y)
            for x in range(self._cols):
                if self._grid[y][x] != '.':
                    continue
                self._grid[y][x] = '#'
                if self.is_looped():
                    obstructions += 1
                self._grid[y][x] = '.'
        return obstructions

def solve_first():
    lab_map = LabMap()
    return lab_map.guard_route()


def solve_second():
    lab_map = LabMap()
    # Takes ~18 seconds to run.
    return lab_map.possible_obstructions()
        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()
