from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int

def dist(p1: Point, p2: Point) -> float:
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2


class UnionSet:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.set_sizes = [1] * n
    
    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        p = self.find(self.parents[x])
        self.parents[x] = p
        return p
    
    def union(self, x: int, y: int):
        px = self.find(x)
        py = self.find(y)
        if px != py:
            self.parents[px] = py
            self.set_sizes[py] += self.set_sizes[px]
    
    def set_size(self, x: int) -> int:
        return self.set_sizes[self.find(x)]


class Circuits:
    def __init__(self, filename):
        with open(filename, 'rt') as f:
            self.points = [
                Point(*map(int, line.strip().split(',')))
                for line in f.readlines()
            ]

        self.us = UnionSet(len(self.points))
        self.dists = sorted(
            (dist(self.points[i], self.points[j]), i, j)
            for i in range(len(self.points))
            for j in range(i + 1, len(self.points))
        )

    def solve_first(self, num_connections):
        n = 0
        connections_made = 0
        while connections_made < num_connections and n < len(self.dists):
            _, i, j = self.dists[n]
            if self.us.find(i) != self.us.find(j):
                self.us.union(i, j)
            connections_made += 1
            n += 1

        set_sizes_dict = {self.us.find(i) : self.us.set_size(i) for i in range(len(self.points))}
        set_sizes = sorted(set_sizes_dict.values(), reverse=True)
        return set_sizes[0] * set_sizes[1] * set_sizes[2]
    
    def solve_second(self):
        for _, i, j in self.dists:
            if self.us.find(i) != self.us.find(j):
                self.us.union(i, j)
            if self.us.set_size(i) == len(self.points):
                return self.points[i].x * self.points[j].x


def main():
    circuits = Circuits('input.txt')
    print(circuits.solve_second())


if __name__ == '__main__':
    main()

