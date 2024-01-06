import re

lines = open("data/4.data.txt", "r").read().split("\n")


def parseLine(line):
    t = tuple(map(lambda s: re.sub(r"\s+", ",", s.strip()), line.split(":")[1].split("|")))
    return tuple(map(lambda s: list(map(int, s.split(","))), t))


def part1():
    s = 0
    for line in lines:
        a, b = parseLine(line)
        w = 0
        for x in a:
            for y in b:
                if x == y:
                    if w == 0: w = 1
                    else: w *= 2
        s += w
    print(s)


def part2():
    counts = [1] * len(lines)
    for i in range(len(lines)):
        a, b = parseLine(lines[i])
        totalMatching = 0
        for x in a:
            for y in b:
                if x == y:
                    totalMatching += 1
        for k in range(i + 1, i + 1 + totalMatching):
            counts[k] += counts[i]
    print(sum(counts))


part2()
