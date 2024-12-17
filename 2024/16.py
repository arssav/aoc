from dataclasses import dataclass


@dataclass(eq=True, frozen=True)
class Position:
    x: int
    y: int
    dx: int
    dy: int

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
INF = int(1e15)


class Maze:
    def __init__(self):
        with open('input.txt', 'rt') as f:
            self._maze = [list(l.strip()) for l in f]
        self._rows = len(self._maze)
        self._cols = len(self._maze[0])
        for y in range(self._rows):
            for x in range(self._cols):
                if self._maze[y][x] == 'S':
                    self._start = (x, y)
                if self._maze[y][x] == 'E':
                    self._end = (x, y)

    def edges(self, pos: Position):
        yield (Position(pos.x + pos.dx, pos.y + pos.dy, pos.dx, pos.dy), 1)
        for dx, dy in DIRS:
            if dx * pos.dx + dy * pos.dy == 0:
                yield (Position(pos.x, pos.y, dx, dy), 1000)

    def reverse_edges(self, pos: Position):
        yield (Position(pos.x - pos.dx, pos.y - pos.dy, pos.dx, pos.dy), 1)
        for dx, dy in DIRS:
            if dx * pos.dx + dy * pos.dy == 0:
                yield (Position(pos.x, pos.y, dx, dy), 1000)


    def fastest_route(self):
        dist: dict[Position, int] = {}
        final_dist: dict[Position, int] = {}
        for y in range(self._rows):
            for x in range(self._cols):
                if self._maze[y][x] == '#':
                    continue
                for dx, dy in DIRS:
                    dist[Position(x, y, dx, dy)] = INF
        dist[Position(self._start[0], self._start[1], 1, 0)] = 0
        while True:
            if len(dist) == 0:
                break
            min_pos = None
            min_dist = INF
            for pos, d in dist.items():
                if d < min_dist:
                    min_dist = d
                    min_pos = pos
            if min_pos is None:
                break
            final_dist[min_pos] = min_dist
            del dist[min_pos]
            for pos, weight in self.edges(min_pos):
                if pos in final_dist:
                    continue
                if self._maze[pos.y][pos.x] == '#':
                    continue
                dist[pos] = min(dist[pos], min_dist + weight)
        min_dist = INF
        for dx, dy in DIRS:
            min_dist = min(min_dist, final_dist.get(Position(self._end[0], self._end[1], dx, dy), INF))
        self._dist = final_dist
        return min_dist
    
    def fill_best_path_cells(self, pos: Position, dist: int):
        self._routes.add((pos.x, pos.y))
        for npos, weight in self.reverse_edges(pos):
            if self._maze[npos.y][npos.x] == '#':
                continue
            if self._dist.get(npos, INF) == dist - weight:
                self.fill_best_path_cells(npos, dist - weight)

    def best_path_cells(self):
        self._routes = set()
        dist = self.fastest_route()
        for dir in DIRS:
            pos = Position(self._end[0], self._end[1], dir[0], dir[1])
            if self._dist[pos] == dist:
                self.fill_best_path_cells(pos, dist)
        return len(self._routes)


def solve_first():
    maze = Maze()
    return maze.fastest_route()

def solve_second():
    maze = Maze()
    return maze.best_path_cells()

def main():
    print(solve_second())


if __name__ == '__main__':
    main()
