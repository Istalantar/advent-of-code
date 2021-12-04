def main():
    with open("input.txt", 'r') as file:
        content = file.read().splitlines()

    part_one(content)
    part_two(content)


def part_one(content):
    index_monitor = []
    was_line_executed = False
    line_index = 0
    accumulator = 0

    while not was_line_executed:
        if 'acc' in content[line_index]:
            if '-' in content[line_index]:
                accumulator -= int(content[line_index][5:])
            elif '+' in content[line_index]:
                accumulator += int(content[line_index][5:])

            index_monitor.append(line_index)
            line_index += 1
        elif 'jmp' in content[line_index]:
            if '-' in content[line_index]:
                line_index -= int(content[line_index][5:])
            elif '+' in content[line_index]:
                line_index += int(content[line_index][5:])

        elif 'nop' in content[line_index]:
            line_index += 1
        else:
            pass

        if line_index in index_monitor:
            print(f'Next intended line has already been executed: {line_index}')
            print(f'Current accumulator value (Part One): {accumulator}')
            was_line_executed = True


def part_two(content):
    for i in range(len(content)):
        edited_code = edit_code(i, content)

        if edited_code != 0:
            execute_code(edited_code)


def edit_code(i: int, code: list):
    """
    swaps jmp for nop or nop for jmp at index i
    :param i:
    line index to edit
    :param code:
    code to edit
    :return:
    returns 0 if code was not edited, or returns edited code
    """
    edited_code = code.copy()

    if 'jmp' in code[i]:
        edited_code[i] = code[i].replace('jmp', 'nop')
    elif 'nop' in code[i]:
        edited_code[i] = code[i].replace('nop', 'jmp')
    else:
        return 0

    return edited_code


def execute_code(content):
    index_monitor = []
    was_line_executed = False
    last_line_found = False
    line_index = 0
    accumulator = 0

    while not was_line_executed and not last_line_found:
        if 'acc' in content[line_index]:
            if '-' in content[line_index]:
                accumulator -= int(content[line_index][5:])
            elif '+' in content[line_index]:
                accumulator += int(content[line_index][5:])

            index_monitor.append(line_index)
            line_index += 1
        elif 'jmp' in content[line_index]:
            if '-' in content[line_index]:
                line_index -= int(content[line_index][5:])
            elif '+' in content[line_index]:
                line_index += int(content[line_index][5:])

        elif 'nop' in content[line_index]:
            line_index += 1
        else:
            pass

        if line_index in index_monitor:
            # print(f'Next intended line has already been executed: {line_index}')
            # print(f'Current accumulator value: {accumulator}')
            was_line_executed = True

        if line_index == (len(content) - 1):
            print(f'Last line in code found: {content[line_index]}')
            print(f'Current accumulator value (Part Two): {accumulator}')
            last_line_found = True


main()
