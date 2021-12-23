def main():
    with open("input.txt", 'r') as file:
        content = file.read().splitlines()

    part_one_index = part_one(content)
    print(f'Part One: {content[part_one_index + 25]} does not have the property. (Index: {part_one_index})')
    print(f'Part Two: Weakness = {part_two(content, part_one_index)}')


def part_one(content):
    offset = 25

    for i in range(len(content)):
        sum_found = False

        for a in content[i:i + offset]:
            for b in content[i:i + offset]:
                if (int(a) + int(b)) == int(content[i + offset]):
                    sum_found = True

        if not sum_found:
            return i


def part_two(content, index):
    weakness = 0

    for i in range(len(content)):
        if int(content[i]) < int(content[index + 25]):
            sum_list = find_sum_list(content, index, i)
        else:
            sum_list = None
        if sum_list is not None:
            sum_list.sort()
            weakness = int(sum_list[0]) + int(sum_list[-1])
            return weakness

    return weakness


def find_sum_list(content, index, i):
    my_sum = 0

    for j in range(i, index + 25):
        my_sum += int(content[j])
        if my_sum == int(content[index + 25]):
            return content[i:j+1]
        elif my_sum > int(content[index + 25]):
            return None

    return None


main()
