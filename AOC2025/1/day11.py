def main():
    currentValue = 50
    password = 0 
    with open ('puzzle.txt', 'r') as f:
        for line in f:
            if line[0] == 'R':
                newValue = currentValue + (int(line[1:]) % 100)
                if newValue >= 100:
                    currentValue = newValue - 100
                else:
                    currentValue = newValue
                if currentValue == 0:
                    password += 1
            else:
                newValue = currentValue - (int(line[1:]) % 100)
                if newValue == 0:
                    password += 1
                if newValue < 0:
                    currentValue = newValue + 100
                else:
                    currentValue = newValue
    print(password)

main()