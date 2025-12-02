import re
import numpy as np

blocks = open("data/13.txt", "r").read().strip().split("\n\n")

def solve(px, py):
    a, b = np.round(np.dot(invm, np.array([px, py])), 2)
    if a - int(a) != 0 or b - int(b) != 0:
        return -1, -1
    return a, b

total1, total2 = 0, 0
for block in blocks:
    l1, l2, l3 = block.split("\n")
    ax, ay = map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", l1)[0])
    bx, by = map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", l2)[0])
    px1, py1 = map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", l3)[0])
    px2, py2 = px1 + 10000000000000, py1 + 10000000000000
    m = np.array([[ax, bx],
                 [ay, by]], dtype=np.int64)
    invm = np.linalg.inv(m)

    a, b = solve(px1, py1)
    if a != -1:
        total1 += 3 * a + b
    a, b = solve(px2, py2)
    if a != -1:
        total2 += 3 * a + b

print("--")
print(total1)
print(total2)
