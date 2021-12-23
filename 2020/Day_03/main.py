
def slope(dy, dx):
    trees = 0
    x = 1
    for y in range(dy, max_lines, dy):
        x += dx
        if x > 31:
            x -= 31

        if lines[y][x-1] == '#':
            trees += 1

    return trees


with open("input.txt", 'r') as file:
    lines = file.readlines()

max_lines = len(lines)
for i in range(max_lines):
    lines[i] = lines[i].strip()

one = slope(1, 1)
two = slope(1, 3)
three = slope(1, 5)
four = slope(1, 7)
five = slope(2, 1)

print(one, two, three, four, five)
print(one * two * three * four * five)
