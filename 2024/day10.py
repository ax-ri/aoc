import numpy as np

grid = np.genfromtxt('data/10.txt', delimiter=1, dtype=int)
h, w = grid.shape
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

def part1():
    def countPaths(y, x, value):
        if value == 9:
            if grid[y, x] == 9:
                return y, x
            else:
                return None

        for d in directions:
            y2, x2 = y + d[0], x + d[1]
            if 0 <= y2 < h and 0 <= x2 < w and grid[y2, x2] == value + 1:
                result.add(countPaths(y2, x2, value + 1))
        return None

    total = 0
    for y in range(h):
        for x in range(w):
            if grid[y, x] == 0:
                result = set()
                countPaths(y, x, 0)
                if None in result:
                    result.remove(None)
                total += len(result)
    print(total)

def part2():
    def countPaths(y, x, value):
        if value == 9:
            if grid[y, x] == 9:
                return 1
            else:
                return 0

        c = 0
        for d in directions:
            y2, x2 = y + d[0], x + d[1]
            if 0 <= y2 < h and 0 <= x2 < w and grid[y2, x2] == value + 1:
                c += countPaths(y2, x2, value + 1)
        return c

    total = 0
    for y in range(h):
        for x in range(w):
            if grid[y, x] == 0:
                total += countPaths(y, x, 0)
    print(total)

part1()
part2()