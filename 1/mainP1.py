
leftArray = []
rightArray = []
distance = 0

with open('input.txt', 'r') as f:
    for line in f:
        left, right = line.split()
        leftArray.append(int(left))
        rightArray.append(int(right))

leftArray.sort()
rightArray.sort()

for i in range(len(leftArray)):
    distance += abs(leftArray[i] - rightArray[i])

print(f"Total distance is: {distance}")