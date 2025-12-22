class TachyonBeams:
    def __init__(self, filename):
        with open(filename, 'rt') as f:
            self.grid = [line.strip() for line in f]
    
    def solve(self, mode='first'):
        beams = []
        for s in self.grid[0]:
            beams.append(1 if s == 'S' else 0)
        splits = 0
        for row in self.grid[1:]:
            new_beams = [0 for _ in beams]
            for i, s in enumerate(row):
                if beams[i] == 0:
                    continue
                if s == '^':
                    new_beams[i - 1] += beams[i]
                    new_beams[i + 1] += beams[i]
                    splits += 1
                else:
                    new_beams[i] += beams[i]
            beams = new_beams
        return splits if mode == 'first' else sum(beams)

def main():
    tachyon_beams = TachyonBeams('input.txt')
    print(tachyon_beams.solve('second'))

if __name__ == '__main__':
    main()
