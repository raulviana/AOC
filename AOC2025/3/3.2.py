
def checkDeletion(indexes, reversed):
    deleted = False
    print (f'Indexes to check: {indexes}')
    for i in indexes:
        print(f'Checking index: {i}, value: {reversed[i]}')
        if i < len(reversed)-1:
            print(f'Checking index: {i}, value: {reversed[i]}, next value: {reversed[i+1]}')
            if reversed[i] < reversed[i+1]:
             del reversed[i]
             print(f'deleted index: {i}, vaLUE: {reversed[i]}')
             deleted = True
             break
    if not deleted:
        print(f'deleted last index: {indexes[-1]}, VALUE: {reversed[indexes[-1]]}')
        del reversed[indexes[-1]]
    return reversed
            

def processBatteries(batteries):
    bat = list(batteries.replace('\n', ''))
    bat = list(map(int, bat))
    while len(bat) > 12:
        reversed = bat[::-1]
        minVAlue = min(reversed)
        indexes =  [i for i,val in enumerate(reversed) if val==minVAlue]
        reversed = checkDeletion(indexes, reversed)
        bat = reversed[::-1]
    bat = list(map(str, bat))
    return ''.join(bat)


total = 0
with open('input.txt') as f:
    for line in f:
        bat = line
        total += int(processBatteries(bat))
        break
print(f'The total sum is: {total}')