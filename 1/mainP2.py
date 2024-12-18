


leftArray = []
rightArray = []
similarity = 0
ocurrences= {}

with open('input.txt', 'r') as f:
    for line in f:
        left, right = line.split()
        leftArray.append(int(left))
        rightArray.append(int(right))

leftArray.sort()
rightArray.sort()

for i in range(len(leftArray)):

    if str(leftArray[i]) in ocurrences:
            similarity += leftArray[i] * int(ocurrences[str(leftArray[i])])
            continue
    else:
        ocurrences[str(leftArray[i])] = 0
        for j in range(len(rightArray)):
            if leftArray[i] == rightArray[j]:
                ocurrences[str(leftArray[i])] += 1
        similarity += leftArray[i] * int(ocurrences[str(leftArray[i])])

print(f"Total similarity is: {similarity}")
                
