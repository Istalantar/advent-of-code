
with open("input.txt", 'r') as file:
    lines = file.readlines()

numbers = [int(str.strip(line)) for line in lines]
numbers.sort()

for a in numbers:
    for b in numbers:
        for c in numbers:
            if a + b + c == 2020:
                print(f'{a} * {b} * {c} = {a*b*c}')
                exit(0)
