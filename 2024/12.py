class Garden:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            self._grid = [list(l.strip()) for l in f]
        self._visited = set()
        self._fence_graph = None
    
    def is_valid_coordinate(self, x, y):
        return x >= 0 and x < len(self._grid[0]) and y >= 0 and y < len(self._grid)
    
    def neighbors(self, x, y):
        yield (x + 1, y)
        yield (x - 1, y)
        yield (x, y + 1)
        yield (x, y - 1)
    
    def region_params(self, x, y):
        if (x, y) in self._visited:
            return 0, 0
        if not self.is_valid_coordinate(x, y):
            return 0, 0
        self._visited.add((x, y))
        area = 1
        perimeter = 0
        for x1, y1 in self.neighbors(x, y):
            if not self.is_valid_coordinate(x1, y1):
                perimeter += 1
                continue
            if self._grid[y1][x1] == self._grid[y][x]:
                a, p = self.region_params(x1, y1)
                area += a
                perimeter += p
            else:
                perimeter += 1
        return area, perimeter

    
    def compute_cost(self):
        total = 0
        for y in range(len(self._grid)):
            for x in range(len(self._grid[0])):
                if (x, y) in self._visited:
                    continue
                area, perimeter = self.region_params(x, y)
                total += area * perimeter

        return total
    
    def node_knots(self, x, y):
        for dx in range(2):
            for dy in range(2):
                yield (x + dx, y + dy)

    def knot_nodes(self, x, y):
        for dx in range(2):
            for dy in range(2):
                yield (x - dx, y - dy)

    def record_knot_neighbors(self, x, y, label):
        if (x, y) in self._knot_neighbors:
            return
        self._knot_neighbors[(x, y)] = 0
        for node in self.knot_nodes(x, y):
            if self.is_valid_coordinate(node[0], node[1]) and self._grid[node[1]][node[0]] == label:
                self._knot_neighbors[(x, y)] += 1

    def walk_region(self, x, y):
        if (x, y) in self._visited:
            return 0
        if not self.is_valid_coordinate(x, y):
            return 0
        self._visited.add((x, y))
        self._current_region.add((x, y))
        for knot in self.node_knots(x, y):
            self.record_knot_neighbors(knot[0], knot[1], self._grid[y][x])
        area = 1
        for x1, y1 in self.neighbors(x, y):
            if self.is_valid_coordinate(x1, y1) and self._grid[y1][x1] == self._grid[y][x]:
                a = self.walk_region(x1, y1)
                area += a
        return area
    
    def diagonal_corners_for_knot(self, x, y, label):
        if x <= 0 or x >= len(self._grid[0]) or y <= 0 or y >= len(self._grid):
            return 0
        if self._knot_neighbors[(x, y)] != 2:
            return 0
        if self._grid[y][x] == self._grid[y - 1][x - 1] and self._grid[y][x] == label:
            if (x, y) in self._current_region and (x - 1, y - 1) in self._current_region:
                return 2
            else:
                return 1
        if self._grid[y][x - 1] == self._grid[y - 1][x] and self._grid[y][x - 1] == label:
            if (x - 1, y) in self._current_region and (x, y - 1) in self._current_region:
                return 2
            else:
                return 1
        return 0

    
    def compute_bulk_cost(self):
        total = 0
        for y in range(len(self._grid)):
            for x in range(len(self._grid[0])):
                if (x, y) in self._visited:
                    continue
                self._knot_neighbors = {}
                self._current_region = set()
                area = self.walk_region(x, y)
                sides = 0
                for knot, neighbors in self._knot_neighbors.items():
                    if neighbors % 2:
                        sides += 1
                    sides +=  self.diagonal_corners_for_knot(knot[0], knot[1], self._grid[y][x])
                total += area * sides

        return total


def solve_first():
    garden = Garden()
    return garden.compute_cost()

def solve_second():
    garden = Garden()
    return garden.compute_bulk_cost()

        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()
