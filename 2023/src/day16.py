import numpy as np
import collections

dirs = {
    "r": (0, 1),
    "l": (0, -1),
    "u": (-1, 0),
    "d": (1, 0)
}


def isHorizontal(d):
    return d == "l" or d == "r"


def rotated(d, plus):
    if d == "l":
        return "d" if plus else "u"
    elif d == "r":
        return "u" if plus else "d"
    elif d == "u":
        return "r" if plus else "l"
    elif d == "d":
        return "l" if plus else "r"


lines = open("data/16.data.txt", "r").read().split("\n")
grid = np.array([list(line) for line in lines])
h, w = grid.shape


def findPath(startPoint, startDir):
    toProcess = collections.deque()
    toProcess.append((startPoint, startDir))

    seen = set()
    energized = set()

    while toProcess:
        (y0, x0), d = toProcess.pop()

        energized.add((y0, x0))

        dy, dx = dirs[d]
        y, x = y0 + dy, x0 + dx
        if y < 0 or y >= h or x < 0 or x >= w:
            continue

        if grid[(y, x)] == "." and ((y, x), d) in seen:
            continue
        seen.add(((y, x), d))

        u = (y, x)
        v = (y, x)

        if grid[v] == ".":
            toProcess.append(((y, x), d))
        elif grid[u] == "/":
            toProcess.append(((y, x), rotated(d, True)))
        elif grid[u] == "\\":
            toProcess.append(((y, x), rotated(d, False)))
        elif grid[u] == "|":
            if isHorizontal(d):
                toProcess.append(((y, x), "u"))
                toProcess.append(((y, x), "d"))
            else:
                toProcess.append(((y, x), d))
        elif grid[u] == "-":
            if isHorizontal(d):
                toProcess.append(((y, x), d))
            else:
                toProcess.append(((y, x), "l"))
                toProcess.append(((y, x), "r"))

    return len(energized) - 1


def part1():
    print(findPath((0, -1), "r"))


def part2():
    starts = []
    starts += [((-1, x), "d") for x in range(w)]
    starts += [((h, x), "u") for x in range(w)]
    starts += [((y, -1), "r") for y in range(h)]
    starts += [((y, w), "l") for y in range(h)]

    m = -1
    for (startPoint, startDir) in starts:
        pathLen = findPath(startPoint, startDir)
        if pathLen > m:
            m = pathLen
    print(m)


part2()
