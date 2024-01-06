import re

lines = open("data/3.data.txt", "r").read().split("\n")


def isSymbol(c):
    return c != "." and not c.isdecimal()


def part1():
    s, size = 0, len(lines)
    for i in range(size):
        for m in re.finditer(r"\d+", lines[i]):
            isPart = False
            start, end = m.span()
            for j in range(i - 1, i + 2):
                for k in range(start - 1, end + 1):
                    if (0 < j < size) and (0 < k < len(lines[i])) and isSymbol(lines[j][k]):
                        isPart = True
            if isPart:
                print(m.group())
                s += int(m.group())
    print(s)


def part2():
    gears = {}
    size = len(lines)
    for i in range(size):
        for m in re.finditer(r"\d+", lines[i]):
            start, end = m.span()
            for j in range(i - 1, i + 2):
                for k in range(start - 1, end + 1):
                    if (0 < j < size) and (0 < k < len(lines[i])) and lines[j][k] == "*":
                        gears.setdefault((j, k), [])
                        gears[(j, k)].append(int(m.group()))
    s = 0
    for gear in gears.values():
        print(gear)
        if len(gear) == 2:
            s += gear[0] * gear[1]
    print(s)


part2()
