lines = open("data/7.txt", "r").read().split("\n")

def check(numbers, current, goal):
    l = len(numbers)
    if l == 0:
        return False

    x = numbers[0]
    if x + current == goal:
        return True
    if x * current == goal:
        return True
    if int(str(current) + str(x)) == goal:
        return True

    if check(numbers[1:], x + current, goal):
        return True

    if check(numbers[1:], x * current, goal):
        return True

    if check(numbers[1:], int(str(current) + str(x)), goal):
        return True

    return False

total = 0
for line in lines:
    goal, numbers = line.split(':')
    goal = int(goal)
    numbers = list(map(int, numbers.strip().split(" ")))
    if check(numbers[1:], numbers[0],  goal):
        # print(goal, "ok")
        total += goal

print(total)