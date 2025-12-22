def main():
    rules = []
    updates = []

    with open('input.txt', 'r') as file:
        first_part = True
        for line in file:
            print(line, first_part, line == None)
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
    # for update in updates:
    #     for 









if __name__ == "__main__":
    main()