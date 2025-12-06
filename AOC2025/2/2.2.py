
import textwrap

def checkFakeId(current):
    for i in range(int(len(current) / 2) +1):
        if i == 0: 
            continue
        else:
            exploded = textwrap.wrap(current, i)
            if len(exploded) > 1:
                unique = set()
                unique = unique.union(exploded)
                if len(unique) == 1:
                    print(exploded, unique, current)
                    return int(current)
    return 0





def main():
    ids = []
    with open('input.txt') as f:
        for line in f:
            ids = line.split(',')
    total = 0
    count = 1
    for idsRange in ids:
        print('Processing range: ' + str(count))
        count += 1
        begin = int(idsRange.split('-')[0])
        end = int(idsRange.split('-')[1])
        for i in range(begin, end+1):
            current = str(i)
            total += checkFakeId(current)

    print(total)

main()