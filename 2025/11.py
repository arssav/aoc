from collections import defaultdict

class Reactor:
    def __init__(self, filename):
        self.outs = defaultdict(list)
        with open(filename, 'rt') as f:
            for line in f:
                node, outs = line.strip().split(': ')
                for out in outs.split(' '):
                    self.outs[node].append(out)
        self.num_paths = defaultdict(int)

        self.ins = defaultdict(list)
        for node, outs in self.outs.items():
            for out in outs:
                self.ins[out].append(node)

    def count_paths(self, node):
        if node in self.num_paths:
            return self.num_paths[node]
        else:
            np = 0
            for inp in self.ins[node]:
                np += self.count_paths(inp)
            self.num_paths[node] = np
            return np

    def count_paths_from_to(self, start, end):
        self.num_paths = defaultdict(int)
        self.num_paths[start] = 1
        return self.count_paths(end)

    def solve_first(self):
        return self.count_paths_from_to('you', 'out')
    
    def solve_second(self):
        return (self.count_paths_from_to('svr', 'fft') *
                self.count_paths_from_to('fft', 'dac') *
                self.count_paths_from_to('dac', 'out'))


def main():
    reactor = Reactor("input.txt")
    print(reactor.solve_second())


if __name__ == "__main__":
    main()
