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
    all_the_ways = 0
    is_done = False
    shortest_solution = [0]

    content.sort()
    built_in = content[-1] + 3
    content.append(built_in)
    content.insert(0, 0)

    # immer eine Zahl rausnehmen und schauen, ob die Bedingung noch gilt
    for i in range(1, len(content)-1):
        pass

    i = 0
    # find the shortest solution (biggest possible steps between adapters)
    while not is_done:
        try:
            if (content[i+1] - content[i]) == 3:
                shortest_solution.append(content[i+1])
                i = i + 1
            elif (content[i+2] - content[i]) == 3:
                shortest_solution.append(content[i+2])
                i = i + 2
            elif (content[i+3] - content[i]) == 3:
                shortest_solution.append(content[i+3])
                i = i + 3
            elif (content[i+1] - content[i]) == 2:
                shortest_solution.append(content[i+1])
                i = i + 1
            elif (content[i+2] - content[i]) == 2:
                shortest_solution.append(content[i+2])
                i = i + 2
            elif (content[i+1] - content[i]) == 1:
                shortest_solution.append(content[i+1])
                i = i + 1
            else:
                print(f'Unexpected problem (i = {i})')
        except IndexError:
            # If IndexError occured then the shortest solution must have been found
            is_done = True
            if shortest_solution[-1] != built_in:  # add the built_in value, if it is not yet in the list
                shortest_solution.append(built_in)
            all_the_ways = 1
            print(f'IndexError: i = {i}')

    # find all the other ways

    return f'All the ways to connect the device: {all_the_ways}'


def find_all_the_ways(startindex: int, adapters: []):
    all_the_ways = 0

    for i in range(startindex, len(adapters)):
        pass

    return all_the_ways


main()
