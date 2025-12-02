from functools import cache

stones = list(map(int, open("data/11.txt", "r").read().strip().split(" ")))

@cache
def count(stone, d):
    if d == 0:
        return 1
    if stone == 0:
        return count(1, d - 1)
    digits = str(stone)
    l = len(digits)
    if l % 2 == 0:
        return count(int(digits[:(l // 2)]), d - 1) + count(int(digits[(l // 2):]), d - 1)
    return count(stone * 2024, d - 1)

def solve(n):
    total = 0
    for stone in stones:
        total += count(stone, n)
    return total

print("part 1:", solve(25))
print("part 2:", solve(75))