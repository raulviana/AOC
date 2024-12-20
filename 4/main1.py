
target = 'XMAS'
back_target = 'SAMX'

def main():
    file_content = []

    with open('input.txt', 'r') as file:
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
                total += parse(i, j, file_content)

    print(f"Total: {total}")


def check_return_value(return_value):
    if return_value == target or return_value == back_target:
        return 1
    else:
        return 0
    
def parse(i, j, file_content):
    # j -> horizontal
    # i -> vertical
    sub_total = 0
    return_value = ''
    return_value = go_forward(i, j, 0, file_content, '')
    sub_total += check_return_value(return_value)
    return_value = ''
    return_value = go_back(i, j, target, 0, file_content, '')
    sub_total += check_return_value(return_value)
    return_value = ''
    return_value = go_up(i, j, target, 0, file_content, '')
    sub_total += check_return_value(return_value)
    return_value = ''
    return_value = go_down(i, j, target, 0, file_content, '')
    sub_total += check_return_value(return_value)
    return_value = ''
    return_value = go_forward_up(i, j, target, 0, file_content, '')
    sub_total += check_return_value(return_value)
    return_value = ''
    return_value = go_forward_down(i, j, target, 0, file_content, '')
    sub_total += check_return_value(return_value)
    return_value = ''
    return_value = go_back_up(i, j, target, 0, file_content, '')
    sub_total += check_return_value(return_value)
    return_value = ''
    return_value = go_back_down(i, j, target, 0, file_content, '')
    sub_total += check_return_value(return_value)
    return sub_total


def go_forward(i, j, position, file_content, return_value):
    if j > len(file_content[0]) - 1:
        return return_value
    return_value += file_content[i][j]
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
            return go_forward(i, j + 1, position + 1, file_content, return_value)
    else:
        return return_value
    

def go_back(i, j, target, position, file_content, return_value):
    if j < 0:
        return return_value
    return_value += file_content[i][j]
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
                return go_back(i, j - 1, target, position + 1, file_content, return_value)
    else:
        return return_value

def go_up(i, j, target, position, file_content, return_value):
    return_value += file_content[i][j]
    if i < 0:
        return return_value
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
                return go_up(i - 1, j, target, position + 1, file_content, return_value)
    else:
        return return_value

def go_down(i, j, target, position, file_content, return_value):
    if i > len(file_content) - 1:
        return return_value
    return_value += file_content[i][j]
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
            try:
                return go_down(i + 1, j, target, position + 1, file_content, return_value)
            except IndexError:
                return return_value
    else:
        return return_value

def go_forward_up(i, j, target, position, file_content, return_value):
    if i < 0 or j > len(file_content[0]) - 1:
        return return_value
    return_value += file_content[i][j]
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
            try:
                return go_forward_up(i - 1, j + 1, target, position + 1, file_content, return_value)
            except IndexError:
                return return_value
    else:
        return return_value

def go_forward_down(i, j, target, position, file_content, return_value):
    if i > len(file_content) - 1 or j > len(file_content[0]) - 1:
        return return_value
    return_value += file_content[i][j]
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
            try:
                return go_forward_down(i + 1, j + 1, target, position + 1, file_content, return_value)
            except IndexError:
                return return_value
    else:
        return return_value

def go_back_up(i, j, target, position, file_content, return_value):
    if i < 0 or j < 0:
        return return_value
    return_value += file_content[i][j]
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
            try:
                return go_back_up(i - 1, j - 1, target, position + 1, file_content, return_value)
            except IndexError:
                return return_value
    else:
        return return_value

def go_back_down(i, j, target, position, file_content, return_value):
    if i > len(file_content) - 1 or j < 0:
        return return_value
    return_value += file_content[i][j]
    if file_content[i][j] == target[position]:
        if position == len(target) -1:
            return return_value
        else:
            try:
                return go_back_down(i + 1, j - 1, target, position + 1, file_content, return_value)
            except IndexError:
                return return_value
    else:
        return return_value


if __name__ == "__main__":
    main()