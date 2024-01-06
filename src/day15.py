line = open("data/15.data.txt", "r").read().strip()


def computeHash(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h %= 256
    return h


def part1():
    s = 0
    for seq in line.split(","):
        s += computeHash(seq)
    print(s)


def part2():
    boxes = {}
    for seq in line.split(","):
        if "-" in seq:
            label = seq.split("-")[0]
            box = computeHash(label)
            if box in boxes:
                newContent = []
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] != label:
                        newContent.append(boxes[box][i])
                boxes[box] = newContent
        else:
            label, focal = seq.split("=")
            box = computeHash(label)
            focal = int(focal)
            if box in boxes:
                exists = False
                for i in range(len(boxes[box])):
                    if boxes[box][i][0] == label:
                        boxes[box][i][1] = focal
                        exists = True
                        break
                if not exists:
                    boxes[box].append([label, focal])
            else:
                boxes[box] = [[label, focal]]

    s = 0
    for i in range(max(boxes.keys()) + 1):
        if i not in boxes:
            continue
        for j in range(len(boxes[i])):
            s += (i + 1) * (j + 1) * boxes[i][j][1]
    print(s)


part2()
