from functools import cmp_to_key

rules, updates = open("data/5.txt", "r").read().split("\n\n")
rules = list(map(lambda s: tuple(map(int, s.split("|"))), rules.split("\n")))
updates = list(map(lambda s: list(map(int, s.split(","))), updates.split("\n")))

rulesDict = {}
for (x, y) in rules:
    rulesDict.setdefault(x, [])
    rulesDict[x].append(y)

def compare(a, b):
    if a in rulesDict and b in rulesDict[a]:
        return -1
    else:
        return 0

p1, p2 = 0, 0
for update in updates:
    s = sorted(update, key=cmp_to_key(compare))
    k = len(update) // 2
    if update == s:
        p1 += update[k]
    else:
        p2 += s[k]
print("Part 1: {}\nPart 2: {}".format(p1, p2))

