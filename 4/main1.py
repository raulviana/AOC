
target = 'XMAS'
back_target = 'SAMX'

def main():
    file_content = []

    with open('./4/input.txt', 'r') as file:
        for line in file:
            line = line.replace('\n', '')
            temp_line = []
            temp_line[:] = line
            file_content.append(temp_line)

    length = len(file_content)
    height = len(file_content[0])
    total = 0

    for i in range(length):
        for j in range(height):
            if file_content[i][j] == target[0]:
                total += parse(i, j, length, height, file_content)
        break
    print(f"Total: {total}")

def check_return_value(return_value):
    if return_value == target or return_value == back_target:
        return 1
    else:
        return 0
    
def parse(i, j, length, height, file_content):
    # j -> horizontal
    # i -> vertical
    target_length = len(target) -1
    sub_total = 0
    if j < (length - target_length):
        return_value = go_forward(i, j, 0, file_content, '')
        print(f"Return Value: {return_value}, {check_return_value(return_value)}")
        sub_total = check_return_value(return_value)
    #if j > target_length:
    #    return_value += go_back(i, j, target, 0, file_content)
    #if i > target_length:
    #    return_value += go_up(i, j, target, 0, file_content)
    #if i < (height - target_length):
    #    return_value += go_down(i, j, target, 0, file_content)
    #if j < (length - target_length) and i > target_length:
    #    return_value += go_forward_up(i, j, target, 0, file_content)
    #if j < (length - target_length) and i < (height - target_length):
    #    return_value += go_forward_down(i, j, target, 0, file_content)
    #if j > target_length and i > target_length:
    #    return_value += go_back_up(i, j, target, 0, file_content)
    #if j > target_length and i < (height - target_length):
    #    return_value += go_back_down(i, j, target, 0, file_content)

    return sub_total


def go_forward(i, j, position, file_content, return_value):
    return_value += file_content[i][j]
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
            return go_forward(i, j + 1, position + 1, file_content, return_value)
    else:
        return return_value
    

def go_back(i, j, target, position, file_content):
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return 1
        else:
            return go_back(i, j - 1, target, position + 1, file_content)
    else:
        return 0

def go_up(i, j, target, position, file_content):
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return 1
        else:
            return go_up(i - 1, j, target, position + 1, file_content)
    else:
        return 0

def go_down(i, j, target, position, file_content):
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return 1
        else:
            return go_down(i + 1, j, target, position + 1, file_content)
    else:
        return 0

def go_forward_up(i, j, target, position, file_content):
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return 1
        else:
            return go_forward_up(i - 1, j + 1, target, position + 1, file_content)
    else:
        return 0

def go_forward_down(i, j, target, position, file_content):
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return 1
        else:
            return go_forward_down(i + 1, j + 1, target, position + 1, file_content)
    else:
        return 0

def go_back_up(i, j, target, position, file_content):
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return 1
        else:
            return go_back_up(i - 1, j - 1, target, position + 1, file_content)
    else:
        return 0

def go_back_down(i, j, target, position, file_content):
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return 1
        else:
            return go_back_down(i + 1, j - 1, target, position + 1, file_content)
    else:
        return 0


if __name__ == "__main__":
    main()