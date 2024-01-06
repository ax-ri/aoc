import numpy as np

import time

lines = open("data/14.data.txt", "r").read().split("\n")


def parseC(c):
    return 2 if c == "O" else (1 if c == "#" else 0)


def simulate(grid):
    # print(grid)
    h, w = grid.shape
    for x in range(w):
        for y in range(h):
            if grid[y, x] == 2:
                t = y
                while t > 0 and grid[t - 1, x] == 0:
                    t -= 1
                if grid[t, x] == 0:
                    grid[t, x] = 2
                    grid[y, x] = 0


def computeLoad(grid):
    s = 0
    h, _ = grid.shape
    for y in range(h):
        s += np.count_nonzero(grid[y] == 2) * (h - y)
    return s


def part1():
    grid = np.array([[parseC(c) for c in line] for line in lines])
    simulate(grid)
    print(computeLoad(grid))


def toString(grid):
    h, w = grid.shape
    s = ""
    for y in range(h):
        for x in range(w):
            s += str(grid[y, x])
        s += "\n"
    return s


def part2():
    grid = np.array([[parseC(c) for c in line] for line in lines])
    seen = {}
    k = 0
    tot = 1_000_000_000
    while k < tot - 1:

        for _ in range(4):
            simulate(grid)
            grid = np.rot90(grid, 3)

        s = toString(grid)
        if s in seen:
            print(k, "is like", seen[s])
            k = seen[s] + ((tot - 1 - seen[s]) // (k - seen[s])) * (k - seen[s])
            seen = {}
            print("k jumps to", k)
        else:
            seen[s] = k
            k += 1

    print("Result:", computeLoad(grid))


start = time.time_ns()
part2()
stop = time.time_ns()
print((stop - start) * 1e-9, "s")
