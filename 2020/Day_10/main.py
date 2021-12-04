def main():
    with open("input.txt", 'r') as file:
        content = file.read().splitlines()

    content = [int(x) for x in content]

    print(part_one(content.copy()))
    print(part_two(content.copy()))


def part_one(content):
    one_jolt = 0
    three_jolt = 0

    content.sort()
    built_in = content[-1] + 3
    content.append(built_in)
    content.insert(0, 0)

    for i in range(len(content) - 1):
        diff = content[i + 1] - content[i]
        if diff == 1:
            one_jolt += 1
        elif diff == 3:
            three_jolt += 1
        elif diff == 0:
            print(f'Warning: Two adapters with the same joltage ({content[i]}')
        elif diff == 2:
            pass
        else:
            print(f'Error: Unexpected joltage difference. j1 = {content[i]}, j2 = {content[i + 1]}')

    return f'{one_jolt} * 1-jolts multiplied by {three_jolt} * 3-jolts = {one_jolt * three_jolt}'


def part_two(content):
    content.sort()
    built_in = content[-1] + 3
    content.append(built_in)
    content.insert(0, 0)
    adaptors = content.copy()

    # solution from: https://github.com/anand2312/advent-of-code/blob/main/2020/Python/day_10_task2.py
    path_counts = {adaptors[0]: 1}

    for i in adaptors[1:]:
        my_sum = 0
        for j in range(1, 4):
            my_sum += path_counts.get(i - j, 0)
        path_counts[i] = my_sum

    return path_counts.popitem()[1]


main()
