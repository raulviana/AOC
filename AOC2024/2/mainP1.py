
def process_report(report):
    lastLevel = None
    positive = 0
    for i in range(len(report)):
        if i == 0:
            lastLevel = int(report[i])
            positive = int(report[i]) - int(report[i+1])
        else:
            if lastLevel == int(report[i]):
                return 0
            if (positive > 0 and lastLevel - int(report[i]) < 0) or (positive < 0 and lastLevel - int(report[i]) > 0):
                return 0
            if (abs(lastLevel - int(report[i])) >= 4 or abs(lastLevel - int(report[i])) == 0):
                return 0
        lastLevel = int(report[i])
    return 1


safe = 0
with open('input.txt', 'r') as f:
    for line in f:
        safe += process_report(line.split())

print(f"Safe count is: {safe}")
