

def checkId(ranges, id):
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            return 1
    return 0


with open('input.txt') as f:
    phase = ['ranges', 'ids']
    index = 0
    ranges = []
    total = 0
    for line in f:
        if line.strip() == '' and phase[index] == 'ids':
            ranges.clear()
            index = 0
            continue
        elif line.strip() == '' and phase[index] == 'ranges':
            index = 1
            continue 
        if phase[index] == 'ranges':
            ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))
        else:
            id = int(line)
            total += checkId(ranges, id)

print(f'Total: {total}')
