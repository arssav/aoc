from collections import defaultdict
from math import ceil, log10

class Stones:
    def __init__(self):
        self._stones = defaultdict(int)
        with open('input.txt', 'rt') as f:
            for s in map(int, f.readline().strip().split()):
                self._stones[s] += 1

    def digits_count(self, n):
        return ceil(log10(n + 1))

    def has_even_digits_count(self, n):
        return 0 == (self.digits_count(n) % 2)
    
    def split(self, n):
        d = self.digits_count(n)
        return n // (10 ** (d // 2)), n % (10 ** (d // 2))

    def blink(self):
        new_stones = defaultdict(int)
        for stone, cnt in self._stones.items():
            if stone == 0:
                new_stones[1] += cnt
            elif self.has_even_digits_count(stone):
                a, b = self.split(stone)
                new_stones[a] += cnt
                new_stones[b] += cnt
            else:
                new_stones[stone * 2024] += cnt
        self._stones = new_stones
    
    def count_stones(self, num_blinks):
        for _ in range(num_blinks):
            self.blink()
        return sum(self._stones.values())


def solve_first():
    stones = Stones()
    return stones.count_stones(25)

def solve_second():
    stones = Stones()
    return stones.count_stones(75)

        
def main():
    print(solve_second())

if __name__ == '__main__':
    main()
