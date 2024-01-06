from math import lcm

lines = open("data/8.data.txt", "r").read().split("\n")

moves = lines[0]
moveCount = len(moves)

edges = {}
for line in lines[2:]:
    a, b = line.split(" = ")
    b = b.replace("(", "").replace(")", "")
    edges[a] = b.split(", ")


def applyMove(move, vertex):
    if move == "L":
        return edges[vertex][0]
    else:
        return edges[vertex][1]


def part1():
    i = 0
    s = "AAA"
    while s != "ZZZ":
        s = applyMove(moves[i % moveCount], s)
        i += 1
    print(i)


def part2():
    vertices = [s for s in edges.keys() if s[-1] == "A"]

    n = len(vertices)
    cycleLens = [0] * n

    for k in range(n):
        i = 0
        while True:
            if vertices[k][-1] == "Z":
                cycleLens[k] = i
                break
            vertices[k] = applyMove(moves[i % moveCount], vertices[k])
            i += 1

    print(lcm(*cycleLens))


part1()
part2()
