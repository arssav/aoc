NUM_SHAPES = 6

class Presents:
    def __init__(self, filename):
        with open(filename, 'rt') as f:
            # Not really needed, but left for historical reasons
            for _ in range(NUM_SHAPES):
                f.readline()
                f.readline()
                f.readline()
                f.readline()
                f.readline()
            self.grids = []
            self.nums = []
            for line in f:
                grid_str, num_presents = line.strip().split(': ')
                self.grids.append(list(map(int, grid_str.split('x'))))
                self.nums.append(list(map(int, num_presents.split(' '))))
            

    def solve_first(self):
        max_ans = 0
        for i in range(len(self.grids)):
            grid_area = self.grids[i][0] * self.grids[i][1]
            presents_area = 7 * sum(self.nums[i])
            print(i, grid_area, presents_area, grid_area >= presents_area)
            if grid_area >= presents_area:
                max_ans += 1

        return max_ans

def main():
    presents = Presents('input.txt')
    print(presents.solve_first())

if __name__ == '__main__':
    main()
