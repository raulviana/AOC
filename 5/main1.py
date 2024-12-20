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
                #print(type(line))
                rules.append([int(line[0]), int(line[1])])
            else:
                line = line.strip().split(',')
                line = [int(i) for i in line]
                updates.append(line)

    

    total = 0
    
    for update in updates:
        good = True
        for rule in rules:
            if rule[0] in update and rule[1] in update:           
                if update.index(rule[0]) < update.index(rule[1]):
                    pass
                else:
                    good = False

        if good:
            total += update[(len(update) // 2)]

    print(f"Total: {total}")










if __name__ == "__main__":
    main()