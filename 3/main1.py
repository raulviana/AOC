

import re


file_content = None

with open('./input.txt', 'r') as file:
    file_content = file.read()

muls = re.findall(r'mul\(\d*?,\d*?\)', file_content)

total = 0

for mul in muls:
    a, b = map(int, re.findall(r'\d+', mul))
    total += a * b

print(f"Total: {total}")