import numpy as np

lines = open("data/11.data.txt", "r").read().split("\n")

stars = np.array([[1 if c == "#" else 0 for c in line] for line in lines])


def part1():
    def expand(array):
        expanded = []
        for row in array:
            expanded.append(row)
            if not np.any(row):
                expanded.append(row)
        return np.array(expanded)

    stars = expand(stars)
    stars = expand(stars.T).T

    coords = tuple(zip(*np.nonzero(stars)))
    dists = { u: [] for u in coords }

    for u in coords:
        for v in coords:
            if u == v:
                continue
            d = abs(u[0] - v[0]) + abs(u[1] - v[1])
            dists[u].append(d)

    s = 0
    for u in coords:
        s += sum(dists[u])
    print(int(s / 2))


def part2():
    expCols = []
    expRows = []
    for y in range(len(stars)):
        if not np.any(stars[y]):
            expRows.append(y)
    tmp = stars.T
    for y in range(len(tmp)):
        if not np.any(tmp[y]):
            expCols.append(y)

    coords = tuple(zip(*np.nonzero(stars)))
    dists = {u: [] for u in coords}

    for u in coords:
        for v in coords:
            if u == v:
                continue
            d = abs(u[0] - v[0]) + abs(u[1] - v[1])
            expCount = 0
            for x in expCols:
                if u[1] <= x <= v[1] or v[1] <= x <= u[1]:
                    expCount += 1
            for y in expRows:
                if u[0] <= y <= v[0] or v[0] <= y <= u[0]:
                    expCount += 1
            d += (1_000_000 - 1) * expCount
            dists[u].append(d)

    s = 0
    for u in coords:
        s += sum(dists[u])
    print(int(s / 2))


part2()
