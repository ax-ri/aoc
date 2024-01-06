def parseWorkflows(desc):
    workflows = {}

    for line in desc.split("\n"):
        workflow, rules = line.split("{")
        rules = rules[:-1]
        workflows[workflow] = []
        for rule in rules.split(","):
            if ":" in rule:
                cond, dest = rule.split(":")
                op = "<" if "<" in cond else ">"
                var, n = cond.split(op)
                workflows[workflow].append((var, op, int(n), dest))
            else:
                workflows[workflow].append(("default", "", 0, rule))
        # if len(workflows[workflow]["order"]) > 4:
        #     print("PROBLEM")

    return workflows


def goThrough(parts, workflows):
    workflow = "in"
    while workflow != "A" and workflow != "R":
        for var, op, n, dest in workflows[workflow]:
            if var == "default":
                workflow = dest
            else:
                if (op == "<" and parts[var] < n) or (op == ">" and parts[var] > n):
                    workflow = dest
                    break
    return workflow == "A"


def aux(workflow, workflows, reduced):
    print("== reducing", workflow, "==")
    if workflow in reduced:
        return reduced[workflow]
    else:
        reduced[workflow] = {}
        for var, op, n, dest in workflows[workflow]:
            start, end = 1, 4_000
            print(var, op, n, dest)

            if dest == "R":
                if op == ">":
                    end = n
                else:
                    start = n
            elif dest == "A":
                if op == "<":
                    end = n
                else:
                    start = n
            else:
                result = aux(dest, workflows, reduced)
                print("result", result)
                if var in result:
                    start, end = result[var]
                else:
                    start, end = result["default"]

                if op == "<":
                    start = max(start, n)
                else:
                    end = min(end, n)

            reduced[workflow][var] = (start, end)
        print("reduce", workflow,  "result:", reduced[workflow])
        return reduced[workflow]


def reduceWorkflows(workflows):
    reduced = {}
    workflow = "in"
    aux(workflow, workflows, reduced)
    print(reduced)


def part1():
    desc, instr = open("data/19.data.txt", "r").read().split("\n\n")
    # desc, instr = open("data/test.txt", "r").read().split("\n\n")

    workflows = parseWorkflows(desc)

    s = 0
    for line in instr.split("\n"):
        parts = {}
        partSum = 0
        for affect in line[1:-1].split(","):
            part, val = affect.split("=")
            val = int(val)
            parts[part] = val
            partSum += val
        if goThrough(parts, workflows):
            s += partSum
    print(s)


def part2():
    # desc, _ = open("data/19.data.txt", "r").read().split("\n\n")
    desc, _ = open("data/test.txt", "r").read().split("\n\n")

    workflows = parseWorkflows(desc)
    print(workflows)
    reduceWorkflows(workflows)


part2()
