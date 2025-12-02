import numpy as np

def safeSet(y, x):
    if 0 <= y < h and 0 <= x < w:
        out[y, x] = 1
        return True
    return False

def sgn(x):
    return 1 if x > 0 else -1

grid = np.genfromtxt('data/8.txt', dtype=str, delimiter=1, comments='/')
h, w = grid.shape
out = np.zeros(grid.shape, dtype=int)

for y1 in range(h):
    for x1 in range(w):
        if grid[y1, x1] != '.':
            for y2 in range(h):
                for x2 in range(w):
                    if y2 != y1 and x2 != x1 and grid[y2, x2] == grid[y1, x1]:
                        dy, dx = abs(y2 - y1), abs(x2 - x1)
                        k = 1
                        while safeSet(y1 + k * sgn(y1 - y2) * dy, x1 + k * sgn(x1 - x2) * dx):
                            k += 1
                        k = 1
                        while safeSet(y2 + k * sgn(y2 - y1) * dy, x2 + k * sgn(x2 - x1) * dx):
                            k += 1
                        # print("\n".join([" ".join([str(grid[y, x]) for x in range(w)]) for y in range(h)]))
                        # print("   0   1   2   3   4   5   6   7   8   9   10  11")
                        # print(np.array(
                        #     "\n".join([" ".join(['#' if out[y, x] else ('.' if grid[y, x] == '.' else grid[y, x]) for x in range(w)]) for y
                        #      in range(h)])))
                        # print("---")
out[grid != "."] = 1
print(np.count_nonzero(out))