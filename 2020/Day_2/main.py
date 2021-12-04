
with open("input.txt", 'r') as file:
    lines = file.readlines()

pw_correct = 0
num_lines = len(lines)

for line in lines:
    p1, p2, password = line.strip().split()
    min_num, max_num = p1.split('-')
    min_num = int(min_num)
    max_num = int(max_num)
    letter = str(p2[0])

### First part
    # if (password.count(letter) >= min_num) & (password.count(letter) <= max_num):
    #     pw_correct += 1

### Second Part
    if (password[min_num-1] == letter) ^ (password[max_num-1] == letter):
        pw_correct += 1

print(f'number of passwords: {num_lines}')
print(f'correct passwords: {pw_correct}')
