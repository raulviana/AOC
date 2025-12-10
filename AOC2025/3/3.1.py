
def clean(batteries): 
    if batteries[-1] == '\n':
        batteries = batteries[:-1]
    return batteries

def processBatteries(batteries):
    maxFirst = 0
    maxSecond = 0
    maxIndex = -1
    batteries = clean(batteries)
    print(batteries)
    for i in reversed(range(len(batteries) -1)):
        print(f'forward Checking battery {batteries[i]} at index {i}')
        if int(batteries[i]) >= maxFirst:
            maxFirst = int(batteries[i])
            maxIndex = i
    for j in range(maxIndex +1, len(batteries)):
        print(f'backward Checking battery {batteries[j]} at index {j}')
        if int(batteries[j]) >= maxSecond:
            maxSecond = int(batteries[j])
    print(f'Max first: {maxFirst}, Max second: {maxSecond}')
    return str(maxFirst) + str(maxSecond)  
        

total = 0
with open('input.txt') as f:
    for line in f:
        bat = line
        total += int(processBatteries(bat))
print(f'The total sum is: {total}')
        