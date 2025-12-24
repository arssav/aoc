class MovieTheater:
    def __init__(self, filename):
        with open(filename, 'rt') as f:
            self.red = [tuple(map(int, line.strip().split(','))) for line in f]


    def solve_first(self):
        max_area = 0
        for i in range(len(self.red)):
            for j in range(i + 1, len(self.red)):
                area = (abs(self.red[j][0] - self.red[i][0]) + 1) * (abs(self.red[j][1] - self.red[i][1]) + 1)
                if area > max_area:
                    max_area = area
        return max_area
    

    def segment_intersects_rectangle(self, a, b, ra, rb):
        min_rx = min(ra[0], rb[0])
        min_ry = min(ra[1], rb[1])
        max_rx = max(ra[0], rb[0])
        max_ry = max(ra[1], rb[1])
        min_x = min(a[0], b[0])
        min_y = min(a[1], b[1])
        max_x = max(a[0], b[0])
        max_y = max(a[1], b[1])

        return (max_x > min_rx and min_x < max_rx) and (max_y > min_ry and min_y < max_ry)

    def solve_second(self):
        max_area = 0
        for i in range(len(self.red)):
            for j in range(i + 1, len(self.red)):
                area = (abs(self.red[j][0] - self.red[i][0]) + 1) * (abs(self.red[j][1] - self.red[i][1]) + 1)
                if area <= max_area:
                    continue
                intersects = False
                for k in range(len(self.red)):
                    a, b = self.red[k], self.red[(k + 1) % len(self.red)]
                    if self.segment_intersects_rectangle(a, b, self.red[i], self.red[j]):
                        intersects = True
                        break
                if not intersects:
                    max_area = area
        return max_area


def main():
    movie_theater = MovieTheater('input.txt')
    print(movie_theater.solve_second())

if __name__ == '__main__':
    main()
