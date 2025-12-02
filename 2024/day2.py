import numpy as np


def isLevelValid(level):
    diff = -1 * np.diff(level)
    return (np.all(diff > 0) or np.all(diff < 0)) and np.max(np.abs(diff)) <= 3 and np.min(np.abs(diff)) >= 1


total = 0
lines = open("data/2.txt", "r").read().strip().split("\n")
for line in lines:
    level = np.array(line.split(" "), dtype=int)

    if isLevelValid(level):
        total += 1
    else:
        for k in range(len(level)):
            if isLevelValid(np.delete(level, k)):
                total += 1
                break


print(total)