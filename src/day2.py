import re

parser = re.compile(r"(\d+) (red|green|blue)")
lines = open("data/2.data.txt", "r").read().split("\n")


def part1():
    max = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    s = 0
    for i, line in zip(range(1, len(lines) + 1), lines):
        recs = line.split(":")[1].split("; ")
        possible = True
        for rec in recs:
            for t in parser.findall(rec):
                if int(t[0]) > max[t[1]]:
                    possible = False
        if possible:
            s += i
    print(s)


def part2():
    s = 0
    for i, line in zip(range(1, len(lines) + 1), lines):
        m = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        recs = line.split(":")[1].split("; ")
        for rec in recs:
            for t in parser.findall(rec):
                m[t[1]] = max(m[t[1]], int(t[0]))
        s += m["red"] * m["green"] * m["blue"]
    print(s)


part2()
