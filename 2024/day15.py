import sys, os

import numpy as np
from io import StringIO

np.set_printoptions(threshold=1000000, linewidth=10000)

lines = open('data/15.test.txt', 'r').read().strip().split("\n\n")
grid = (np.genfromtxt(StringIO(lines[0]), delimiter=1, dtype=str, comments='/'))
h, w = grid.shape

_, y, x = np.argwhere([grid == '@'])[0]
grid[y, x] = '.'

directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
moves = list(lines[1].replace("\n", ""))
for move in moves:
    dy, dx = directions[move]
    y2, x2 = y + dy, x + dx
    if 0 <= x2 < w and 0 <= y2 < h:
        if grid[y2, x2] =='#':
            continue
        elif grid[y2, x2] == '.':
            grid[y2, x2] = '@'
            grid[y, x] = '.'
            y, x = y2, x2
            continue
        else:
            y3, x3 = y2, x2
            while grid[y3, x3] == 'O':
                y3, x3 = y3 + dy, x3 + dx
            if grid[y3, x3] == '.':
                grid[y3, x3] = 'O'
                grid[y2, x2] = '@'
                grid[y, x] = '.'
                y, x = y2, x2
total = 0
for y in range(h):
    for x in range(w):
        if grid[y, x] == 'O':
            total += 100 * y + x
print(total)

side = {'<': ']', '>': '['}
compl = {'[': ']', ']': '['}
offset = {'[': 1, ']': -1}
grid2 = np.zeros(shape=(h, w * 2), dtype=str)
grid = (np.genfromtxt(StringIO(lines[0]), delimiter=1, dtype=str, comments='/'))
for y in range(h):
    for x in range(w):
        if grid[y][x] == '#':
            grid2[y, 2 * x] = '#'
            grid2[y, 2*x + 1] = '#'
        elif grid[y][x] == '.':
            grid2[y, 2 * x] = '.'
            grid2[y, 2 * x + 1] = '.'
        elif grid[y][x] == 'O':
            grid2[y, 2 * x] = '['
            grid2[y, 2 * x + 1] = ']'
        else:
            grid2[y, 2 * x] = '@'
            grid2[y, 2 * x + 1] = '.'
print(grid2)
_, y, x = np.argwhere([grid2 == '@'])[0]
grid2[y, x] = '.'
h, w = h, w * 2
for move in moves:
    os.system('clear')
    print(move)
    dy, dx = directions[move]
    y2, x2 = y + dy, x + dx
    if 0 <= x2 < w and 0 <= y2 < h:
        if grid2[y2, x2] =='#':
            print(grid2)
            input()
            continue
        elif grid2[y2, x2] == '.':
            grid2[y2, x2] = '@'
            grid2[y, x] = '.'
            y, x = y2, x2

            print(grid2)
            input()
            continue
        else:
            y3, x3 = y2, x2
            hor = move in ("<", ">")
            if hor:
                while grid2[y3, x3] == side[move]:
                    x3 += dx * 2
                if grid2[y3, x3] == '.':
                    while x3 != x2:
                        grid2[y3, x3] = compl[grid2[y2, x2]]
                        grid2[y3, x3 - dx] = grid2[y2, x2]
                        x3 -= dx * 2
                    grid2[y2, x2] = '@'
                    grid2[y, x] = '.'
                    y, x = y2, x2
            else:
                while grid2[y3, x3] == grid2[y2, x2]:
                    y3 += dy
                if grid2[y3, x3] == '.' and grid2[y3, x3 + offset[grid2[y2, x2]]] == '.':
                    grid2[y3, x3] = grid2[y2, x2]
                    grid2[y3, x3 + offset[grid2[y2, x2]]] = compl[grid2[y2, x2]]
                    grid2[y2, x2 + offset[grid2[y2, x2]]] = '.'
                    grid2[y2, x2] = '@'
                    grid2[y, x] = '.'
                    y, x = y2, x2

            # else:
            #     if grid2[y3, x3] == '.':
            #         grid2[y3, x3] = grid[y2, x2]
            #         grid2[y3, x3 + dx] = ']' if grid[y2, x2] == '[' else ']'
            #         grid2[y2, x2] = '@'
            #         grid2[y3, x2 + dx] = ']' if grid[y2, x2] == '[' else ']'
            #         grid2[y, x] = '.'
            #         y, x = y2, x2
    # print("---")
    print(grid2)
    input()