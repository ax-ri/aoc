data = list(map(int, list(open("data/9.txt", "r").read().strip())))

def part1(decoded):
    h = 0
    r = -1
    while decoded[r] == ".":
        r -= 1

    while h < len(decoded) and h <= len(decoded) + r:
        if decoded[h] == ".":
            decoded[h] = decoded[r]
            decoded[r] = "."
            while decoded[r] == ".":
                r -= 1
        h += 1

def part2(decoded):
    stacked = []
    i = 0
    while i < len(decoded):
        n = decoded[i]
        k = 0
        while i < len(decoded) and decoded[i] == n:
            i += 1
            k += 1
        stacked.append(([n] * k, i - k))
    stacked.reverse()

    for (s, m) in stacked:
        if s[0] == ".":
            continue
        for i in range(len(decoded)):
            if i >= m:
                continue
            done = False
            if decoded[i] == ".":
                l = 1
                while i + l < len(decoded) and decoded[i + l] == ".":
                    l += 1
                if l >= len(s):
                    for j in range(len(s)):
                        decoded[i + j] = s[j]
                    for k in range(m, m + len(s)):
                        decoded[k] = "."
                        k += 1
                    done = True
            if done:
                break

decoded = []

k = 0
toggle = False
for d in data:
    c = "." if toggle else str(k)
    decoded += [c] * d
    if not toggle:
        k += 1
    toggle = not toggle

# part1(decoded)
part2(decoded)

checksum = 0
for k in range(len(decoded)):
    checksum += k * (0 if decoded[k] == "." else int(decoded[k]))
print(checksum)