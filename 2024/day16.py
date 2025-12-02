import numpy as np
import heapq

grid = np.genfromtxt('data/16.txt', delimiter=1, comments='/', dtype=str)
h, w = grid.shape
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
(startY, startX), (endY, endX) = np.argwhere(grid == 'S')[0], np.argwhere(grid == 'E')[0]
grid[startY, startX] = "."
grid[endY, endX] = "."

def calculate_distances(x, y, d):
    distances = np.array([[float('infinity') for x in range(w)] for y in range(h)])
    distances[y, x] = 0

    pq = [(0, (y, x), d)]
    while len(pq) > 0:
        current_distance, (cy, cx), (cdy, cdx) = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[cy, cx]:
            continue

        for dy, dx in directions:
            y2, x2 = cy + dy, cx + dx
            if 0 <= y2 < w and 0 <= x2 < h and grid[y2, x2] == ".":
                distance = current_distance + 1
                if dx != cdx and dy != cdy:
                    if (cdx != 0 and dx == -cdx) or (cdy != 0 and dy == -cdy):
                        distance += 2000
                    else:
                        distance += 1000

                # Only consider this new path if it's better than any path we've
                # already found.
                if distance < distances[y2, x2]:
                    distances[y2, x2] = distance
                    heapq.heappush(pq, (distance, (y2, x2), (dy, dx)))

    return distances

cost = int(calculate_distances(startX, startY, (0, 1))[endY, endX])
print("part 1:", cost)

paths = np.zeros(grid.shape)

def tryPath(x, y):
    if (y, x) == (endY, endX):
        return cost
    if seen[y, x]:
        return cost + 1
    seen[y, x] = True
    for dy, dx in directions:
        y2, x2 = y + dy, x + dx
        if 0 <= y2 < h and 0 <= x2 < w and grid[y2, x2] == ".":
            c = tryPath(x2, y2)
            if c == cost:
                paths[y, x] = 1



for y in range(h):
    for x in range(w):
        if grid[y, x] == '.':
            print(int(calculate_distances(startX, startY, (0, 1))[endY, endX]))
