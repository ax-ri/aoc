lines = open("data/5.data.txt", "r").read().split("\n")

seeds = list(map(int, lines[0].split(": ")[1].strip().split(" ")))
order = ("seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location")


def parseMaps(reverse):
    maps = {}

    a, b = None, None
    for line in lines[2:]:
        if line:
            if line[0].isdecimal():
                t = tuple(map(int, line.split(" ")))
                if reverse:
                    maps[b][a].append(t)
                else:
                    maps[a][b].append(t)
            else:
                a, b = line.split(" map:")[0].split("-to-")
                maps.setdefault(b if reverse else a, {})
                maps[b if reverse else a].setdefault(a if reverse else b, {})
                if reverse:
                    maps[b][a] = []
                else:
                    maps[a][b] = []
    return maps


def part1():
    maps = parseMaps(False)

    res = {}
    for seed in seeds:
        i = 0
        n = seed
        while order[i] != order[-1]:
            m = False
            for r in maps[order[i]][order[i + 1]]:
                if r[1] <= n <= r[1] + r[2] and not m:
                    n = r[0] + (n - r[1])
                    m = True
            i += 1
            res[seed] = n
    print(min(res.values()))


def part2():
    start, end = 5_000_000, 1_000_000_000  # guessed by trying answers

    reversedMaps = parseMaps(True)
    reversedOrder = tuple(reversed(order))

    res = -1
    for location in range(start, end):
        print(location)
        i = 0
        n = location
        while reversedOrder[i] != reversedOrder[-1]:
            m = False
            for r in reversedMaps[reversedOrder[i]][reversedOrder[i + 1]]:
                if r[0] <= n < r[0] + r[2] and not m:
                    n = r[1] + (n - r[0])
                    m = True
            i += 1
        for j in range(0, len(seeds), 2):
            if 0 <= n - seeds[j] <= seeds[j + 1]:
                res = location
        if res != -1:
            break
    print("Result:", res)


part2()
