import numpy as np

lists = np.loadtxt("data/1.txt", dtype=int)
l1, l2 = lists[:,0], lists[:,1]

def part1():
    l1.sort(); l2.sort()
    print(np.sum(np.abs(l1 - l2)))

def part2():
    total = 0
    for n in l1:
        p = np.count_nonzero(l2 == n)
        total += n * p
    print(total)

part2()