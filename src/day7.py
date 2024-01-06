import functools

lines = open("data/7.data.txt", "r").read().split("\n")

FIVE, FOUR, FULL, THREE, TWO, ONE, HIGH = 20, 19, 18, 17, 16, 15, 14

# order = { '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13 }
order = { 'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13 }


def handType(hand):
    occ = {}
    for c in hand:
        occ.setdefault(c, 0)
        occ[c] += 1

    if "J" in hand:
        if hand == "JJJJJ":
            return FIVE
        occ[max(occ.keys(), key=lambda x: occ[x] if x != "J" else 0)] += hand.count("J")
        del occ["J"]

    l = len(occ)
    if l == 1:
        return FIVE
    if l == 2:
        for c in occ:
            if occ[c] == 1:
                return FOUR
        return FULL
    if l == 3:
        for c in occ:
            if occ[c] == 3:
                return THREE
        return TWO
    if l == 4:
        return ONE
    return HIGH


def cmp(a, b):
    ta, tb = handType(a), handType(b)
    if ta > tb:
        return 1
    if ta < tb:
        return -1

    for i in range(5):
        c = order[a[i]] - order[b[i]]
        if c > 0:
            return 1
        if c < 0:
            return -1

    return 0


bids = {}
for line in lines:
    hand, bid = line.split(" ")
    bids[hand] = int(bid)

bid = 0
for i, hand in zip(range(len(bids)), sorted(bids.keys(), key=functools.cmp_to_key(cmp))):
    bid += (i + 1) * bids[hand]
print(bid)