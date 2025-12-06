
ids = []
with open('input.txt') as f:
    for line in f:
        ids = line.split(',')
total = 0
count = 0
for idsRange in ids:
    print('Processing range: ' + str(count))
    count += 1
    begin = int(idsRange.split('-')[0])
    end = int(idsRange.split('-')[1])
    for i in range(begin, end+1):
        current = str(i)
        if (len(current) % 2 == 0):
            first = current[0:len(current)//2]
            second = current[len(current)//2:]
            if (first == second):
                total += i
print(total)