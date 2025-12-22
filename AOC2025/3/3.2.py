
from typing import List

K = 12

def max_number_after_removals(nums: List[int]) -> int:
    """
    Removes exactly k elements from nums (preserving order)
    to form the maximum possible collapsed number.
    """

    stack = []
    k = len(nums) - K
    for digit in nums:
        # Remove smaller previous digits if we can improve the number
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # If removals remain, remove from the end
    if k > 0:
        stack = stack[:-k]

    # Collapse digits into a number
    return int("".join(map(str, stack)))
            

total = 0
with open('input.txt') as f:
    for line in f:
        bat = line
        bat = list(line.replace('\n', ''))
        bat = list(map(int, bat))
        total += max_number_after_removals(bat)
print(f'The total sum is: {total}')