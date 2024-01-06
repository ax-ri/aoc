import re

lines = open("data/6.data.txt", "r").read().split("\n")


def part1():
    parser = re.compile(r"(\d+)")

    time = list(map(int, parser.findall(lines[0])))
    dist = list(map(int, parser.findall(lines[1])))

    p = 1
    for i in range(len(time)):
        v = 0
        s = 0
        for holdTime in range(time[i]):
            if (time[i] - holdTime) * v > dist[i]:
                s += 1
            v += 1
        p *= s
    print(p)


def part2():
    time = int(re.sub(r"\s+", "", lines[0].split(":")[1]))
    dist = int(re.sub(r"\s+", "", lines[1].split(":")[1]))

    s = 0
    v = 0
    for holdTime in range(time):
        if (time - holdTime) * v > dist:
            s += 1
        v += 1
    print(s)


part2()
