import numpy as np
# from queue import Queue
from collections import deque

# import shapely

lines = open("data/10.data.txt", "r").read().split("\n")
# lines = open("data/test.txt", "r").read().split("\n")

grid = np.array([[c for c in line] for line in lines])
# print(grid)

height, width = len(grid), len(grid[0])

#   N
# W   E
#   S
acceptedDirs = {
    "|": ("N", "S"),
    "-": ("W", "E"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("S", "W"),
    "F": ("S", "E"),
    ".": (),
    "S": ("N", "S", "E", "W")
}

oppositeDirs = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E"
}

dirs = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1)
}

dirFromValue = {
    (-1, 0): "N",
    (1, 0): "S",
    (0, 1): "E",
    (0, -1): "W"
}

start = None
toProcess = deque()
for y in range(height):
    for x in range(width):
        if grid[y, x] == "S":
            start = (y, x)
            toProcess.append((y, x))


def part1():
    seen = set()
    pred = {}
    while len(toProcess) != 0:
        y0, x0 = toProcess.pop()
        if (y0, x0) in seen:
            continue
        seen.add((y0, x0))
        case = grid[y0, x0]
        # print(y0, x0, case)

        for nextCase in acceptedDirs[case]:
            dy, dx = dirs[nextCase]
            y, x = y0 + dy, x0 + dx
            if y < 0 or y > height or x < 0 or x > width:
                continue
            if (y, x) in seen:
                continue
            ok = False
            for prevCase in acceptedDirs[grid[y, x]]:
                if prevCase == oppositeDirs[nextCase]:
                    ok = True
            if ok:
                toProcess.appendleft((y, x))
                pred[(y, x)] = (y0, x0)

    def dist(v0):
        stack = deque()
        stack.append(v0)
        d = 0
        while len(stack) != 0:
            v = stack.pop()
            if v == start:
                break
            d += 1
            stack.append(pred[v])
        return d
    print(max(map(dist, pred)))


def area(p):
    return 0.5 * abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in segments(p)))


def segments(p):
    return zip(p, p[1:] + [p[0]])


#   N
# W   E
#   S
rotations = {
    "N": {
        "E": -1,
        "W": 1
    },
    "S": {
        "E": 1,
        "W": -1
    },
    "E": {
        "N": 1,
        "S": -1
    },
    "W": {
        "N": -1,
        "S": 1
    }
}

rotated = {
    "N": {
        -1: "E",
        1: "W"
    },
    "S": {
        -1: "W",
        1: "E"
    },
    "E": {
        -1: "S",
        1: "N"
    },
    "W": {
        -1: "N",
        1: "S"
    }
}

nextDirs = {
    "|": {"N": "S", "S": "N"},
    "-": {"W": "E", "E": "W"},
    "L": {"N": "E", "E": "N"},
    "J": {"N": "W", "W": "N"},
    "7": {"S": "W", "W": "S"},
    "F": {"S": "E", "E": "S"},
    # "S": ("N": "S", "S": "N", "E", "W")
}

# def nextDir(a, b, prevDir):
#     if b == "|" or b == "-":
#         return prevDir
#     if b == "F":
#         if a == ""

import PIL


np.set_printoptions(linewidth=100000)

def part2():
    seen = set()
    pred = {}
    while len(toProcess) != 0:
        y0, x0 = toProcess.pop()
        if (y0, x0) in seen:
            continue
        seen.add((y0, x0))
        case = grid[y0, x0]
        # print(y0, x0, case)

        for curDir in acceptedDirs[case]:
            dy, dx = dirs[curDir]
            y, x = y0 + dy, x0 + dx
            if y < 0 or y >= height or x < 0 or x >= width:
                continue
            if (y, x) in seen:
                continue
            ok = False
            for nextDir in acceptedDirs[grid[y, x]]:
                if nextDir == oppositeDirs[curDir]:
                    ok = True
                    # print("ok for", nextDir, grid[y, x], y, x)
            if ok:
                toProcess.append((y, x))
                pred[(y, x)] = (y0, x0)

    # path = list(pred.keys())
    # path.append(start)
    # print(path, len(path))
    # print(pred)
    y0, x0 = start
    for dir in acceptedDirs["S"]:
        dy, dx = dirs[dir]
        y, x = y0 + dy, x0 + dx
        if (y, x) in pred and pred[(y, x)] != start and oppositeDirs[dir] in acceptedDirs[grid[y, x]]:
            pred[start] = (y, x)

    print(start)
    print(pred[start])
    # return

    # offset = -1 if start[1] > width / 2 else 1
    # print(offset)
    # ignoredDir = "W" if offset == 1 else "E"

    # area = 0
    # seen = set()

    vertices = [start]
    s = start
    while True:
        s = pred[s]
        if s == start:
            break
        vertices.append(s)
    print(vertices[:3])

    dirOk = set()
    for d in ("N", "S", "E", "W"):
        dy, dx = dirs[d]
        y, x = start[0] + dy, start[1] + dx
        if oppositeDirs[d] in acceptedDirs[grid[(y, x)]]:
            dirOk.add(d)
    repl = ""
    for c in acceptedDirs.keys():
        allOk = True
        for d in dirOk:
            if not d in acceptedDirs[c]:
                allOk = False
        if allOk:
            repl = c
            break
    print(repl)
    grid[start] = repl

    for y0 in range(height):
        for x0 in range(width):
            if (y0, x0) not in vertices:
                grid[(y0, x0)] = "."

    print(grid)

    s = 0
    for y0 in range(height):
        intern = False
        x0 = 0
        while x0 < width:
            c = grid[y0, x0]
            if c == ".":
                if intern:
                    s += 1
            elif c == "|":
                intern = not intern
            elif c == "F":
                while x0 < width and grid[(y0, x0)] not in ("J", "7"):
                    x0 += 1
                if grid[(y0, x0)] == "J":
                    intern = not intern
            elif c == "L":
                while x0 < width and grid[(y0, x0)] not in ("J", "7"):
                    x0 += 1
                if grid[(y0, x0)] == "7":
                    intern = not intern
            x0 += 1
    print("Answer", s)




    # s = 0
    # for y0 in range(height):
    #     intern = False
    #     for x0 in range(width):
    #         if (y0, x0) in vertices:
    #             c = grid[(y0, x0)]
    #             if c != '-':
    #                 intern = not intern
                # if c == "|":
                #     intern = not intern
                # if c == "F":
                #     ext = True
                # if c == "L":
                #     ext = True
                # if c == "7":
                #     if ext:
                #         ext = True
                # if c == "J":
                #     ext = not ext
            # else:
            #     if intern:
            #         s += 1
            #         print(y0, x0, grid[y0, x0])
    # print(s)

    # return
    # L = ("N", "S", "E", "W")
    # # L = "E"
    # #
    # for t in L:
    #     tmp = np.copy(grid)
    #     n = t
    #     u, v = vertices[0], vertices[1]
    #     dy, dx = v[0] - u[0], v[1] - u[1]
    #     prevDir = dirFromValue[(dy, dx)]
    #     for i in range(0, len(vertices) - 1):
    #         u, v = vertices[i], vertices[i + 1]
    #         dy, dx = v[0] - u[0], v[1] - u[1]
    #         # print(nextDir(grid[u], grid[v], n))
    #         # print()
    #         curDir = dirFromValue[(dy, dx)]
    #         # print(nextDir)
    #         if curDir != prevDir:
    #             r = rotations[prevDir][curDir]
    #             n = rotated[n][r]
    #             # print(grid[u], "New norm:", n)
    #         prevDir = curDir
    #         dy, dx = dirs[n]
    #         y, x = u
    #         y += dy; x += dx
    #         if 0 <= y < height and 0 <= x < width and not (y, x) in vertices:
    #             tmp[(y, x)] = "I"
                # y += dy; x += dx
    #
    #     # for line in tmp:
    #     #     print("".join(line))
    #
    #     # print("here")
    #
    #     out = np.zeros(shape=(height, width), dtype=float)
    #
    #     for y0 in range(height):
    #         # print(y0)
    #         for x0 in range(width):
    #             if (y0, x0) in vertices:
    #                 out[y0, x0] = 0
    #             elif tmp[y0, x0] == "I":
    #                 out[y0, x0] = 0.5
    #             else:
    #                 out[y0, x0] = 1
    #
    #     f = open("tmp.txt", "w")
    #     for line in out:
    #         f.write(",".join(map(str, line)) + "\n")
    #
    #     return
    #
    #     for y0 in range(height):
    #         # print(y0)
    #         for x0 in range(width):
    #             if tmp[y0, x0] == "I":
    #                 for d in ("N", "S", "E", "W"):
    #                     dy, dx = dirs[d]
    #                     y, x = y0, x0
    #                     y += dy
    #                     x += dx
    #                     while 0 <= y < height and 0 <= x < width and not (y, x) in vertices:
    #                         tmp[y, x] = "I"
    #                         y += dy
    #                         x += dx
    #
    #     print("there")
    #
    #

        # pb = False
        #
        # def aux(y0, x0):
        #     toProcess = deque()
        #     toProcess.append((y0, x0))
        #
        #     while len(toProcess) != 0:
        #         y0, x0 = toProcess.pop()
        #         tmp[(y0, x0)] = "I"
        #
        #         for d in ("N", "S", "E", "W"):
        #             dy, dx = dirs[d]
        #             y, x = y0 + dy, x0 + dx
        #             if x < 0 or x >= width or y < 0 or y >= height:
        #                 raise RuntimeError()
        #             if tmp[(y, x)] == ".": #or tmp[(y, x)] == "I":
        #                 toProcess.append((y, x))
        #
        # try:
        #     for y0 in range(height):
        #         for x0 in range(width):
        #             if tmp[(y0, x0)] == "I":
        #                 aux(y0, x0)
        # except RuntimeError:
        #     pb = True

        # print(tmp)
        # if pb:
        #     print("I count: WRONG DIR")
        # else:
        #     unique, counts = np.unique(tmp, return_counts=True)
        #     d = dict(zip(unique, counts))
        #     d.setdefault("I", 0)
        #     print("I count:", d["I"])

    #     if s in seen:
    #         continue
    #
    #     if ignoredDir in acceptedDirs[grid[s]]:
    #         continue
    #
    #     x = s[1] + offset
    #     while 0 <= x < width and (s[0], x) not in pred.keys():
    #         print((s[0], x))
    #         x += offset
    #     if 0 <= x < width:
    #         seen.add((s[0], x))
    #         print(x, s[1])
    #         area += abs(x - s[1])
    #     # print(s)
    # print(area)

    # n = 0
    # seen = set()
    # for v in vertices:
    #     for v2 in vertices:
    #         if (v2, v) in seen:
    #             continue
    #         if v == v2:
    #             continue
    #         if pred[v] == v2 or pred[v2] == v:
    #             continue
    #         if v[1] == v2[1] and abs(v[0] - v2[0]) == 1:
    #             print(v, v2)
    #             seen.add((v, v2))
    #             n += 1
    #         if v[0] == v2[0] and abs(v[1] - v2[1]) == 1:
    #             print(v, v2)
    #             seen.add((v, v2))
    #             n += 1
    #         if abs(v[0] - v2[0]) == 1 and abs(v[1] - v[0]) == 1:
    #             print(v, v2)
    #             seen.add((v, v2))
    #             n += 1
    # print("n", n)
    #
    # p = shapely.Polygon(vertices)
    # print(p.area)
    # print(p.length)
    #
    # print(p.area - n)

    # print(len(vertices))
    # print(area(vertices))


part2()
