def main():
    rules = []
    updates = []

    with open('input.txt', 'r') as file:
        first_part = True
        for line in file:
            if len(line.strip()) == 0:
                first_part = False
                continue
            if first_part:
                line = line.replace('|', ',')
                line = line.split(',')
                rules.append([int(line[0]), int(line[1])])
            else:
                line = line.strip().split(',')
                line = [int(i) for i in line]
                updates.append(line)

    total = 0
    
    for update in updates:
        if not check_good(update, rules):
            total += process_not_good(update, rules)

    print(f"Total: {total}")


def check_good(update, rules):
    good = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:           
            if update.index(rule[0]) < update.index(rule[1]):
                pass
            else:
                good = False

    if not good:
        return False
    else:
        return True

def process_not_good(update, rules):
    copy = update.copy()
    count = 0
    while not check_good(update, rules) or count < 100:
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]
        count += 1
    if not check_good(update, rules):
        exit(-1)
    else:
        return update[(len(update) // 2)]




if __name__ == "__main__":
    main()