import bisect
import itertools

class Cafeteria:
    def __init__(self, filename):
        self.ranges = []
        self.ingredients = []
        with open(filename, 'rt') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if '-' in line:
                    l, r = map(int, line.split('-'))
                    self.ranges.append((l, r))
                else:
                    self.ingredients.append(int(line))
    
    def make_ranges_non_overlapping(self):
        ends = sorted(itertools.chain(*[
            [(l, -1), (r, 1)]
            for (l, r) in self.ranges
        ]))
        self.ranges = []
        open_ranges = 0
        last_l = None
        for e in ends:
            if open_ranges == 0 and e[1] == -1:
                last_l = e[0]
            elif open_ranges == 1 and e[1] == 1:
                self.ranges.append((last_l, e[0]))
            open_ranges -= e[1]

    def solve_first(self):
        self.make_ranges_non_overlapping()
        self.left_ends = [l for (l, _) in self.ranges]
        num_fresh = 0
        for i in self.ingredients:
            closest_range = bisect.bisect_right(self.left_ends, i) - 1
            if closest_range < 0:
                continue
            if self.ranges[closest_range][0] <= i <= self.ranges[closest_range][1]:
                num_fresh += 1
        return num_fresh
    
    def solve_second(self):
        self.make_ranges_non_overlapping()
        return sum(r - l + 1 for (l, r) in self.ranges)    

def main():
    cafeteria = Cafeteria('input.txt')
    print(cafeteria.solve_second())


if __name__ == '__main__':
    main()
