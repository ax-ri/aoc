import numpy as np
import shapely

lines = open("data/test.txt", "r").read().split("\n")


directions = {
    "R": (0, 1),
    "L": (0, -1),
    "D": (1, 0),
    "U": (-1, 0)
}


def computeArea(parser):
    y0, x0 = 0, 0
    vertices = [(y0, x0)]

    for line in lines:
        d, count = parser(line)
        count = int(count)

        dy, dx = directions[d]
        y, x = y0 + dy * (count), x0 + dx * (count)

        vertices.append((y, x))

        y0, x0 = y, x

    poly = shapely.Polygon(vertices)
    return int(poly.area + 1 + poly.length / 2)


def parse1(line):
    d, count, _ = line.split(" ")
    count = int(count)
    return d, count


dirOrder = ["R", "D", "L", "U"]


def parse2(line):
    hexStr = line.split("#")[1][:-1]
    dirIndex = int(hexStr[-1])
    d = dirOrder[dirIndex]
    count = int(hexStr[:-1], 16)
    return d, count


def part1():
    print(computeArea(parse1))


def part2():
    print(computeArea(parse2))


part2()
