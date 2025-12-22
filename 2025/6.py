from operator import mul
from functools import reduce

class CephalopodMath:
    def __init__(self, filename):
        with open(filename, 'rt') as f:
            self.lines = f.readlines()

    def solve_first(self):
        number_lines = []
        for l in self.lines[:-1]:
            number_lines.append(
                list(map(int, filter(None, l.strip().split(' '))))
            )

        self.operations = list(filter(None, self.lines[-1].strip().split(' ')))
        self.numbers = [[l[x] for l in number_lines] for x in range(len(number_lines[0]))]

        total = 0
        for i in range(len(self.operations)):
            if self.operations[i] == '+':
                total += sum(self.numbers[i])
            else:
                total += reduce(mul, self.numbers[i], 1)
        return total
    
    def solve_second(self):
        total = 0
        numbers = []
        op = None
        for i in range(len(self.lines[0])):
            if self.lines[-1][i] not in (' ', '\n'):
                op = self.lines[-1][i]
            if all(l[i] in (' ', '\n') for l in self.lines):
                if op == '+':
                    total += sum(numbers)
                else:
                    total += reduce(mul, numbers, 1)
                numbers = []
            else:
                numbers.append(int(''.join(l[i] for l in self.lines[:-1])))

        return total


def main():
    cephalopod_math = CephalopodMath('input.txt')
    print(cephalopod_math.solve_second())

if __name__ == '__main__':
    main()
