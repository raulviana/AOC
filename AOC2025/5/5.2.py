

def processRanges(ranges, total):
    mergedRanges = [[ranges[0][0], ranges[0][1]]]
    print(len(ranges))
    for i in range(1, len(ranges)):
        if mergedRanges[-1][1] >= ranges[i][0] and mergedRanges[-1][1] >= ranges[i][1]:
            continue
        if mergedRanges[-1][1] < ranges[i][0]:
            mergedRanges.append(ranges[i])
            continue
        if mergedRanges[-1][1] >= ranges[i][0] and mergedRanges[-1][1] < ranges[i][1]:
            mergedRanges[-1][1] = ranges[i][1]
            
    print(len(mergedRanges))
    for mergedRange in mergedRanges:
        total += mergedRange[1] - mergedRange[0] + 1
    return total
        

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
            ranges.append([int(line.split('-')[0]), int(line.split('-')[1])])
        else:
            continue

ranges.sort(key=lambda x: x[0])
total = processRanges(ranges, total)
print(f'Total: {total}')