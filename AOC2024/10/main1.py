

def main():
    file_content = []
    with open('input.txt', 'r') as file:
        for line in file:
            line_ints = [int(i) for i in line.strip()]
            file_content.append(line_ints)
    total = 0
    for i in range(0, len(file_content)):
        for j in range(0, len(file_content[i])):
            # i vertical, j horizontal
            if file_content[i][j] == 0:
                total += process_trail(file_content, i, j)
                print('total', total)
        break
    print(total)
def process_trail(file_content, i, j, curernt_height=-1):
    print('i,j', i,j, 'curernt_height', curernt_height)
    if file_content[i][j] != curernt_height + 1 or i < 0 or i >= len(file_content) or j < 0 or j >= len(file_content[i]):
        return 0
    
    if file_content[i][j] == 9:
        return 1
    
    curernt_height = file_content[i][j]
    print(i,j)
    if i - 1 >= 0:
        process_trail(file_content, i-1, j, curernt_height)
    if i + 1 < len(file_content):
        process_trail(file_content, i+1, j, curernt_height)
    if j - 1 >= 0:
        process_trail(file_content, i, j-1, curernt_height)
    if j + 1 < len(file_content[i]):
        process_trail(file_content, i, j+1, curernt_height)







if __name__ == "__main__":
    main()