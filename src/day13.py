import numpy as np

# grids = open("data/test.txt", "r").read().split("\n\n")
grids = open("data/13.data.txt", "r").read().split("\n\n")


def findAxe(grid):
    h, w = grid.shape
    alt = []
    for y in range(h):
        dy = min(y, h - 1 - y)
        top = grid[y-dy:y+1] if y <= h // 2 else grid[y-1-dy:y]
        bot = np.flip(grid[y+1:y+1+dy+1] if y <= h // 2 else grid[y:y+dy+1], axis=0)
        if top.shape == bot.shape and np.all(top == bot):
            alt.append(y if y > h // 2 else y + 1)
    return alt


def part1():
    sV, sH = 0, 0
    for grid in grids:
        grid = np.array([[1 if c == "#" else 0 for c in row] for row in grid.split("\n")])
        alt = findAxe(grid)
        if not alt:
            alt = findAxe(grid.T)
            sV += alt[0]
        else:
            sH += alt[0]
    print(100 * sH + sV)


def part2():
    sV, sH = 0, 0
    for grid in grids:
        grid = np.array([[1 if c == "#" else 0 for c in row] for row in grid.split("\n")])

        altH0, altV0 = findAxe(grid), findAxe(grid.T)
        altH0 = altH0[0] if len(altH0) == 1 else -1
        altV0 = altV0[0] if len(altV0) == 1 else -1

        h, w = grid.shape
        stop = False

        for y in range(h):
            if stop:
                break
            for x in range(w):
                if stop:
                    break

                grid[y, x] = 1 - grid[y, x]

                altH, altV = findAxe(grid), findAxe(grid.T)

                if altH0 in altH:
                    altH.remove(altH0)
                if altV0 in altV:
                    altV.remove(altV0)

                if altH:
                    sH += altH[0]
                    stop = True
                if altV:
                    sV += altV[0]
                    stop = True

                grid[y, x] = 1 - grid[y, x]
    print(100 * sH + sV)


part2()
