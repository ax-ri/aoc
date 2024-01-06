import numpy as np

lines = open("data/9.data.txt", "r").read().split("\n")

records = np.array([list(map(int, line.split(" "))) for line in lines])


def compute(index, coeff):
    s = 0
    for rec in records[:]:
        diffs = [rec]
        while diffs[-1].any():
            diffs.append(np.diff(diffs[-1]))

        n = 0
        for i in range(len(diffs) - 2, -1, -1):
            n = diffs[i][index] + coeff * n
        s += n
    return s


def part1():
    print(compute(-1, 1))


def part2():
    print(compute(0, -1))


part2()
