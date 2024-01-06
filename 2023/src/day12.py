import numpy as np
from itertools import groupby
from functools import cache
import time


# lines = open("data/test.txt", "r").read().split("\n")
lines = open("data/12.data.txt", "r").read().split("\n")


def group(symbols):
    return [len(list(v)) for k, v in groupby(symbols) if k == 1]


def groupCount(symbols):
    return len(group(symbols))


def check(symbols, counts):
    return group(symbols) == counts


def naif(symbols, counts):
    # print(symbols)

    if symbols.count(2) == 0:
        return 1 if check(symbols, counts) else 0

    i = 0
    while i < len(symbols) and symbols[i] != 2:
        i += 1
    if i == len(symbols):
        return 0
    else:
        symbols[i] = 0
        n = naif(symbols, counts)
        symbols[i] = 1
        n += naif(symbols, counts)
        symbols[i] = 2
        return n

    # for i in range(len(symbols)):
    #     if symbols[i] == 2:
    #         symbols[i] = 0
    #         s += naif(symbols, counts)
    #         symbols[i] = 1
    #         s += naif(symbols, counts)
    #         symbols[i] = 2
    #
    # print(symbols)
    #
    # print("checking")
    # print("s=", s)
    # if check(symbols, counts):
    #     return 1 + s
    # else:
    #     return 0


def arrayReplaced(array, pattern, repl):
    cp = list(array)
    for i in range(len(array)):
        if array[i] == pattern:
            cp[i] = repl
    return cp


def naif2(symbols, counts, maxSharp):

    if symbols.count(2) == 0:
        return 1 if check(symbols, counts) else 0

    i = 0
    while i < len(symbols) and symbols[i] != 2:
        i += 1
    if i == len(symbols):
        return 0
    else:
        symbols[i] = 0
        n = naif(symbols, counts)
        if symbols.count(1) < maxSharp:
            symbols[i] = 1
            n += naif(symbols, counts)
        symbols[i] = 2
        return n


def opti(symbols, counts):
    maxSharp = sum(counts)
    return naif2(symbols, counts, maxSharp)


    # print(symbols, counts)
    # t = 0
    # maxSharp = sum(counts)
    # for i in range(len(symbols)):
    #     if symbols.count(1) > maxSharp:
    #         break
    #     if symbols[i] == 2:
    #         symbols[i] = 1
    #         if groupCount(arrayReplaced(symbols, 2, 0)) != len(counts):
    #             symbols[i] = 0
    # print(symbols)
    #
    # return 0


def part1():
    s = 0
    for line in lines:
        symbols, counts = line.split(" ")
        symbols = [1 if s == "#" else (2 if s == "?" else 0) for s in symbols]
        counts = list(map(int, counts.split(",")))
        n = naif(symbols, counts)
        s += n
    print(s)


def part2():
    s = 0
    for line in lines[:1]:
        symbols, counts = line.split(" ")

        symbols = "?".join([symbols] * 5)
        counts = ",".join([counts] * 5)

        symbols = [1 if s == "#" else (2 if s == "?" else 0) for s in symbols]
        counts = tuple(map(int, counts.split(",")))

        # print(symbols, counts)

        # n = naif(symbols, counts)
        n = opti(symbols, counts)
        print("n =", n)
        s += n
    print(s)


start = time.time_ns()
part2()
stop = time.time_ns()
print(f"{(stop - start) * 1e-6} ms")

# for line in lines:
#     symbols, counts = line.split(" ")
#     print(check([1 if s == "#" else 0 for s in symbols], list(map(int, counts.split(",")))))
