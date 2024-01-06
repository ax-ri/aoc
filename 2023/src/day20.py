import queue

lines = open("data/20.data.txt", "r").read().split("\n")
# lines = open("data/test.txt", "r").read().split("\n"):


def parseModules():
    modules = {}
    for line in lines:
        m, dest = line.split(" -> ")
        t = "b" if m == "broadcaster" else "F" if m[0] == "%" else "C"
        if m != "broadcaster":
            m = m[1:]
        n = dest.replace(" ", "").split(",")
        modules[m] = [t, n, False, {}]

    for m in modules:
        for n in modules[m][1]:
            if n not in modules:
                continue
            if modules[n][0] == "C":
                modules[n][3][m] = False
    return modules


modules = parseModules()


def simulatePush(callback):
    toProcess = queue.Queue()
    toProcess.put(("button", False, "broadcaster"))

    while not toProcess.empty():
        source, pulse, dest = toProcess.get()
        # print(source, "-high" if pulse else "-low", "->", dest)

        if callback(pulse, dest):
            exit()

        if dest not in modules:
            continue
        type_, neighbors, state, _ = modules[dest]

        if dest == "broadcaster":
            for neighbor in neighbors:
                toProcess.put((dest, pulse, neighbor))
        elif type_ == "F":
            if not pulse:
                modules[dest][2] = not state
                for neighbor in neighbors:
                    toProcess.put((dest, not state, neighbor))
        elif type_ == "C":
            modules[dest][3][source] = pulse
            allHigh = True
            for m in modules[dest][3]:
                if not modules[dest][3][m]:
                    allHigh = False
                    break
            for neighbor in neighbors:
                toProcess.put((dest, not allHigh, neighbor))


counts = {False: 0, True: 0}


def updateCount(pulse, _):
    counts[pulse] += 1
    return False


def part1():
    for _ in range(1000):
        simulatePush(updateCount)
    print(counts[False] * counts[True])


def check(pulse, dest):
    return not pulse and dest == "rx"


def part2():
    for i in range(1, 100_000_000_000):
        print(i)
        simulatePush(check)


part1()
