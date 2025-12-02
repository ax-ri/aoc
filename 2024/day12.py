import numpy as np
import shapely

grid = np.genfromtxt('data/12.test.txt', delimiter=1, dtype=str)
h, w = grid.shape
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

regions = {}
seen = np.zeros(grid.shape)
def explore(x, y, prefix):
    if seen[y, x]:
        return
    seen[y, x] = True
    key = grid[y, x] + prefix
    regions.setdefault(key, {"area": 0, "perimeter": 0, "all-points": [], "border-points": []})
    regions[key]["area"] += 1
    regions[key]["perimeter"] += 4
    # regions[key]["all-points"].append((y, x))

    c = 0
    for dx, dy in directions:
        y2, x2 = y + dy, x + dx
        if 0 <= y2 < h and 0 <= x2 < w and grid[y2, x2] == grid[y, x]:
            regions[key]["perimeter"] -= 1
            c += 1
            explore(x2, y2, prefix)
    if c != 4:
        regions[key]["border-points"].append((y, x))
    else:
        for dx, dy in ((1, 1), (-1, -1), (-1, 1), (1, -1)):
            y2, x2 = y + dy, x + dx
            if 0 <= y2 < h and 0 <= x2 < w and grid[y2, x2] != grid[y, x]:
                regions[key]["border-points"].append((y, x))

for y in range(h):
    for x in range(w):
        explore(x, y, "_{}-{}".format(y, x))
print("\n".join(["{}: {}".format(x, regions[x]) for x in regions]))
total = 0
for r in regions:
    # points = regions[r]["points"]
    # if len(points) == 1:
    #     continue
    # poly = shapely.Polygon(points)
    # print(r, regions[r]["points"])
    # sides = set()
    corners = 0
    for (bpy, bpx) in regions[r]["border-points"]:
        c = [False, False, False, False]
        for k in range(len(directions)):
            dy, dx = directions[k]
            y, x = bpy + dy, bpx + dx
            if (y, x) in regions[r]["border-points"]:
                c[k] = True
        if (c[0] and c[1]) or (c[0] and c[3]) or (c[2] and c[1]) or (c[2] and c[3]):
            corners += 1
            print(bpy, bpx)
    # print(corners)
                # sides.add("{}_{},{}".format(y + 100 if x == bpx else x, dy, dx))
    # print(r, sides, len(sides))
    print(corners)
    print("-----")
    total += regions[r]["area"] * regions[r]["perimeter"]
print(total)