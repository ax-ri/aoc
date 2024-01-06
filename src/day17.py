import numpy as np
import collections
import queue
import heapdict

from heapq import *


dirs = {
    "r": (0, 1),
    "l": (0, -1),
    "u": (-1, 0),
    "d": (1, 0)
}

dirsFromDelta = {
    (0, 1): "r",
    (0, -1): "l",
    (-1, 0): "u",
    (1, 0): "d"
}

oppositeDirs = {
    "l": "r",
    "r": "l",
    "u": "d",
    "d": "u"
}


def rotated(d, plus):
    if d == "l":
        return "d" if plus else "u"
    elif d == "r":
        return "u" if plus else "d"
    elif d == "u":
        return "r" if plus else "l"
    elif d == "d":
        return "l" if plus else "r"


lines = open("data/test.txt", "r").read().split("\n")

grid = np.array([list(map(int, list(line))) for line in lines])
h, w = grid.shape

draw = np.array([list(line) for line in lines])

print(grid)

start, end = (0, 0), (h - 1, w - 1)

# lastDirs = {}


def f():
    def findLastDir(y, x):
        u = (y, x)
        v = prev.get(u, None)
        if v is None:
            return "", 0

        d = dirsFromDelta[u[0] - v[0], u[1] - v[1]]
        c = 0
        # v = prev.get(v, None)
        while v is not None and u != start:
            delta = u[0] - v[0], u[1] - v[1]
            if delta == (0, 0):
                break
            if d == dirsFromDelta[delta]:
                c += 1
            else:
                break
            u, v = v, prev.get(v)
        return d, c

    toProcess = heapdict.heapdict()

    dist = {
        start: 0
    }
    prev = {
        start: start
    }

    for y in range(h):
        for x in range(w):
            if (y, x) != start:
                dist[(y, x)] = 1_000_000_000
                prev[(y, x)] = None
            toProcess[(y, x)] = dist[(y, x)]
    while len(toProcess) != 0:
        (y0, x0), p = toProcess.popitem()
        # lastDir, count = findLastDir(y0, x0)
        # nextDirs = [rotated(lastDir, True), rotated(lastDir, False)] if lastDir else list(dirs.keys())
        # if count < 3 and lastDir:
        #     nextDirs.append(lastDir)
        # if lastDir and nextDir == oppositeDirs[lastDir]:
        #     print("-> ret")
        #     continue
        # if lastDir and lastDir == nextDir and count > 2:
        #     print("-> COUNT", count)
        #     continue
        # print("yes")
        for nextDir in dirs:

            # if count != 0 and lastDir != nextDir:
            #     print(y0, x0, lastDir, nextDir, count)
            # print(lastDir, nextDir, count)
            # print(y0, x0, lastDir, nextDir, count)
            dy, dx = dirs[nextDir]
            y, x = y0 + dy, x0 + dx
            if y < 0 or y >= h or x < 0 or x >= w:
                continue

            old = prev[(y, x)]
            prev[(y, x)] = (y0, x0)
            lastDir, count = findLastDir(y, x)
            prev[(y, x)] = old
            if nextDir == oppositeDirs[lastDir]:
                continue
            if lastDir == nextDir and count >= 4:
                continue
            print(prev.get((y, x), None), (y, x), lastDir, nextDir, count, end=" ")

            alt = p + grid[(y, x)]
            if alt < dist[(y, x)]:
                print("better:", alt)
                dist[(y, x)] = alt
                prev[(y, x)] = (y0, x0)
                toProcess[(y, x)] = alt
            else:
                print("nope")
    s = 0
    u = end
    while u != start and u is not None:
        # print("u is", u)
        s += grid[u]
        draw[u] = "#"
        if u in prev:
            u = prev[u]
        else:
            break
    print()
    print("\n".join([" ".join([c for c in line]) for line in draw]))
    print(s)


# print(dist)
# print(prev)



# toProcess.put((0, (start, 0, "r")))
# toProcess.put((0, (start, 0, "d")))
# stop = False
#
# seen = set()
# pred = {}
# dist = {
#     start: 0
# }
#
# lastDirs = {
#     start: []
# }
#
# toProcess.put((0, start))
#
# while not toProcess.empty():
#     p, (y0, x0) = toProcess.pop()
#     for nextDir in dirs.keys():
#         lastDirs.setdefault((y0, x0), [])
#         if nextDir in lastDirs[(y0, x0)]:
#             continue
#         lastDirs[(y0, x0)].append(nextDir)
#         dy, dx = dirs[nextDir]
#         y, x = y0 + dy, x0 + dx
#         if y < 0 or y >= h or x < 0 or x >= w:
#             continue
#
#         alt = dist.get((y0, x0), 100) + grid[(y, x)]
#         if alt < dist.get((y, x), 100):
#             dist[(y, x)] = alt
#             pred[(y, x)] = (y0, x0)
#
#         toProcess.pu

#
# print(grid)
#
# print(pred)
#
# for u in pred:
#     draw[u] = 0
#
# u = (h - 2, w - 1)


# def dijkstra(s, t):
#     M = set()
#     d = {s: 0, (0, 1): 0, (1, 0): 0}
#     p = { (0, 1): s, (1, 0): s}
#     suivants = [(0, ((0, 1), "r", 1)), (0, ((1, 0), "d", 1))]
#
#     while suivants:
#
#         dx, (u, lastDir, count) = heappop(suivants)
#         print(u, lastDir, count)
#         if u in M:
#             continue
#         M.add(u)
#
#         for nextDir in dirs:
#             if nextDir == oppositeDirs[lastDir]:
#                 continue
#             if nextDir == lastDir and count >= 3:
#                 continue
#             dy, dx = dirs[nextDir]
#             y, x = u[0] + dy, u[1] + dx
#             if y < 0 or y >= h or x < 0 or x >= w:
#                 continue
#             v = (y, x)
#             if v in M:
#                 continue
#             dy = dx + grid[v]
#             if v not in d or d[v] > dy:
#                 d[v] = dy
#                 heappush(suivants, (dy, (v, lastDir, count + (1 if lastDir == nextDir else 0))))
#                 p[v] = u
#
#     print("p", p)
#, nextDir, (count + 1) if lastDir == nextDir else 1)
#     path = [t]
#     x = t
#     while x != s:
#         try:
#             x = p[x]
#         except KeyError:
#             break
#         path.insert(0, x)
#
#     return path
#
#
# path = dijkstra(start, end)
# s = 0
# for u in path:
#     print(u)
#     s += grid[u]
#     draw[u] = 0
# print(s)
#
# print(draw)

import os


def g():
    seen = set()
    toProcess = [(0, ("l", 1, start)), (0, ("u", 1, start))]

    dist = {
        ("l", 1, start): 0,
        ("u", 1, start): 0
    }
    prev = {start: None}

    stop = False

    while len(toProcess) != 0:
        distU, vertex = heappop(toProcess)

        if vertex in seen:
            continue
        seen.add(vertex)

        lastDir, count, u = vertex

        print(distU, vertex)

        for nextDir in dirs:

            if nextDir == oppositeDirs[lastDir]:
                continue

            if lastDir == nextDir and count > 3:
                continue

            dy, dx = dirs[nextDir]
            y, x = u[0] + dy, u[1] + dx

            if x < 0 or x >= w or y < 0 or y >= h:
                continue

            v = (y, x)

            # if v == end:
            #     stop = True
            #     prev[end] = u
            # if stop:
            #     break

            nextVertex = (nextDir, (count + 1) if nextDir == lastDir else count, v)
            if nextVertex in seen:
                continue

            # print(lastDir, nextDir, u, v, count)

            distV = distU + grid[v]
            # print(distV)

            if nextVertex not in dist or distV < dist[nextVertex]:
                dist[nextVertex] = distV
                print(vertex, "->", nextVertex, lastDir, "->", nextDir)
                heappush(toProcess, (distV, nextVertex))
                prev[v] = u
        if stop:
            break

        # os.system("clear")
        # draw = np.array([list(line) for line in lines])
        # a = u
        # print(grid)
        # while a != start and a is not None:
        #     # print("u is", u)
        #     draw[a] = "#"
        #     if a in prev:
        #         a = prev[a][0]
        #     else:
        #         break
        # print()
        # print("\n".join([" ".join([c for c in line]) for line in draw]))
        # print()
        # print(toProcess)
        # input("")
    print(prev)

    print("here")

    draw = np.array([list(line) for line in lines])
    s = 0
    u = end
    seen = set()
    while u != start and u is not None:
        # print("u is", u)
        s += grid[u]
        draw[u] = "#"
        # print(u)
        if u in prev:
            u = prev[u]
        else:
            break
        if u in seen:
            break
        seen.add(u)
    print()
    print("\n".join([" ".join([c for c in line]) for line in draw]))
    print(s)


g()
