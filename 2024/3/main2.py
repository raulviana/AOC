

import re


file_content = None

with open('./2024/3/input.txt', 'r') as file:
    file_content = file.read()

muls = re.findall(r'mul\(\d*?,\d*?\)|do\(\)|don\'t\(\)', file_content)

total = 0

do = 'do()'
do_not = 'don\'t()'
skip = False

for mul in muls:
    if mul == do:
        skip = False
        continue
    elif mul == do_not:
        skip = True
        continue
    else:
        if not skip:
            a, b = map(int, re.findall(r'\d+', mul))
            total += a * b

print(f"Total: {total}")