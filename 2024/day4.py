import numpy as np

# part 1
import re

a = np.genfromtxt("data/4.txt", dtype=str, delimiter=1)

s = ""
dim = a.shape[0]
for i in range(4):
    s += ",".join(["".join(a[j, :]) for j in range(dim)])
    s += ",".join(["".join(a.diagonal(j)) for j in range(-dim + 1, dim)])
    a = np.rot90(a)
print(len(re.findall(r"XMAS", s)))

# part 2
import scipy

lines = open("data/4.txt", "r").read().split("\n")
grid = np.array([[ord(c) for c in line] for line in lines])
kernel = np.array([[1 / ord('M'), 0, 1 / ord('S')],
          [0, 1 / ord('A'), 0],
          [1 / ord('M'), 0, 1 / ord('S')]])
kernels = [np.rot90(kernel, k) for k in range(4)]
count = 0
for kernel in kernels:
    conv = scipy.signal.convolve2d(grid, kernel, mode='valid')
    count += np.count_nonzero(conv == 5)
print(count)

