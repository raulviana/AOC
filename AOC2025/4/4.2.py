

map = []
total = 0
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0), (1, 1)]
 
def check(map, x, y):
    level = 0
    for direction in directions:
        dx, dy = direction
        nx, ny = x + dx, y + dy
        if x == 0 and dx == -1:
            continue
        if y == 0 and dy == -1:
            continue
        if x == len(map) - 1 and dx == 1:
            continue
        if y == len(map[x]) - 1 and dy == 1:
            continue
        if map[nx][ny] == '@':
            level += 1
    return level

with open('input.txt') as f:
    for line in f:
        map.append(list(line.strip()))
y = 0
x = 0
while y < len(map):
    print(f'Processing line {y} of {len(map)}, curernt tolas = {total}')
    while x < len(map[y]):
        if map[x][y] != '@':
            x = x + 1
            continue
        level = 0
        level += check(map, x, y)
        if level < 4:
            total += 1
            map[x][y] = '.'
            if x > 0:
                x = x - 1
            if y > 0:
                y = y - 1
        else:
            x = x + 1
    x = 0
    y = y + 1
            


print(f'Total: {total}')
