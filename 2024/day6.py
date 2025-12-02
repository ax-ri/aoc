import numpy as np

grid = np.genfromtxt('data/6.txt', dtype=str,  delimiter=1, comments='/')
out = np.copy(grid)
grid[grid == '.'] = 0
grid[grid == '#'] = 1
y0, x0 = np.argwhere(grid == '^')[0]
grid[grid == '^'] = 0
grid = grid.astype(np.int8)
h, w = grid.shape
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

maxit = 1_000
total = 0
for yobst in range(h):
    print(yobst, h)
    for xobst in range(w):
        if grid[yobst][xobst] != 0 or (yobst, xobst) == (y0, x0):
            continue
        grid[yobst][xobst] = 1
        y, x = y0, x0
        d = 0  # up
        i = 0
        while 0 <= x < w and 0 <= y < h and i < maxit:
            while grid[y][x] == 0:
                # out[y][x] = 'X'
                y += dirs[d][0]
                x += dirs[d][1]
                if  x < 0 or x >= w or y < 0 or y >= h:
                    break
                if grid[y][x] != 0:
                    y -= dirs[d][0]
                    x -= dirs[d][1]
                    break
            d = (d + 1) % len(dirs)
            i += 1
        grid[yobst][xobst] = 0
        # print(i)
        if i >= maxit:
            total += 1
            # out[yobst][xobst] = 'O'
        # print(np.count_nonzero(out == 'X'))
        # print(grid)
print(total)