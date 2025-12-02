import re
from functools import reduce
from operator import mul
import PIL.Image
import numpy as np

lines = open("data/14.txt", "r").read().strip().split("\n")
# h, w = 7, 11
h, w = 103, 101

data = []

for line in lines:
    px, py, vx, vy = map(int, re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)[0])
    data.append({"px": px, "py": py, "vx": vx, "vy": vy})

for k in range(10000):
    for i in range(len(data)):
        data[i]["px"] = (data[i]["px"] + data[i]["vx"]) % w
        data[i]["py"] = (data[i]["py"] + data[i]["vy"]) % h
    img = np.zeros((w, h, 3), dtype=np.uint8)
    for i in range(len(data)):
        img[data[i]["px"], data[i]["py"]] = (255, 0, 1)
    # print(img)
    PIL.Image.fromarray(img, mode="RGB").save("out/p{}.png".format(k))

    if k == 99:
        counts = [0, 0, 0, 0]
        for i in range(len(data)):
            if data[i]["px"] < w // 2:
                if data[i]["py"] < h // 2:
                    counts[0] += 1
                elif data[i]["py"] > h // 2:
                    counts[1] += 1
            elif data[i]["px"] > w // 2:
                if data[i]["py"] < h // 2:
                    counts[2] += 1
                elif data[i]["py"] > h // 2:
                    counts[3] += 1
        print(counts)
        print(reduce(mul, counts))