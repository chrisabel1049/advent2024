def checkIfUpdateIsGood(update, rules):
    good = True
    for i in range(len(update) - 1, 0, -1):
        for el in update[:i]:
            if update[i] not in rules:
                continue
            if el in rules[update[i]]:
                good = False
                break
    return good


# f = open("testinput.txt", "r")
f = open("actualinput.txt", "r")
rules = {}
updates = []
for line in f.readlines():
    if "|" in line:
        k, v = map(int, line.split("|"))

        if k in rules:
            rules[k].append(v)
        else:
            rules[k] = [v]
    elif line == "\n":
        continue
    else:
        inputUpdate = list(map(int, line.split(",")))
        updates.append(inputUpdate)

print(rules)
sum = 0
for u in updates:
    if checkIfUpdateIsGood(u, rules):
        sum += u[len(u) // 2]

print(sum)
