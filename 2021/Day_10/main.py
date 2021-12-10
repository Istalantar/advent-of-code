import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    my_list = []

    for line in content:
        list_open = []

        for i, symbol in enumerate(line):
            is_wrong = False
            illegal = ''

            if symbol == '(':
                list_open.append(symbol)
            elif symbol == ')':
                if list_open[-1] != '(':
                    illegal = ')'
                    is_wrong = True
                else:
                    list_open.pop(-1)
            elif symbol == '[':
                list_open.append(symbol)
            elif symbol == ']':
                if list_open[-1] != '[':
                    illegal = ']'
                    is_wrong = True
                else:
                    list_open.pop(-1)
            elif symbol == '{':
                list_open.append(symbol)
            elif symbol == '}':
                if list_open[-1] != '{':
                    illegal = '}'
                    is_wrong = True
                else:
                    list_open.pop(-1)
            elif symbol == '<':
                list_open.append(symbol)
            elif symbol == '>':
                if list_open[-1] != '<':
                    illegal = '>'
                    is_wrong = True
                else:
                    list_open.pop(-1)

            if is_wrong and illegal == ')':
                my_list.append(3)
                break
            elif is_wrong and illegal == ']':
                my_list.append(57)
                break
            elif is_wrong and illegal == '}':
                my_list.append(1197)
                break
            elif is_wrong and illegal == '>':
                my_list.append(25137)
                break

    return sum(my_list)


def part_two(content) -> int:
    score = []

    for line in content.copy():
        list_open = []

        for i, symbol in enumerate(line):
            is_wrong = False

            if symbol == '(':
                list_open.append(symbol)
            elif symbol == ')':
                if list_open[-1] != '(':
                    is_wrong = True
                else:
                    list_open.pop(-1)
            elif symbol == '[':
                list_open.append(symbol)
            elif symbol == ']':
                if list_open[-1] != '[':
                    is_wrong = True
                else:
                    list_open.pop(-1)
            elif symbol == '{':
                list_open.append(symbol)
            elif symbol == '}':
                if list_open[-1] != '{':
                    is_wrong = True
                else:
                    list_open.pop(-1)
            elif symbol == '<':
                list_open.append(symbol)
            elif symbol == '>':
                if list_open[-1] != '<':
                    is_wrong = True
                else:
                    list_open.pop(-1)

            if is_wrong and line in content:
                content.remove(line)

    for line in content.copy():
        list_open = []

        for symbol in line:
            if symbol == '(':
                list_open.append(symbol)
            elif symbol == ')' and list_open[-1] == '(':
                list_open.pop(-1)
            elif symbol == '[':
                list_open.append(symbol)
            elif symbol == ']' and list_open[-1] == '[':
                list_open.pop(-1)
            elif symbol == '{':
                list_open.append(symbol)
            elif symbol == '}' and list_open[-1] == '{':
                list_open.pop(-1)
            elif symbol == '<':
                list_open.append(symbol)
            elif symbol == '>' and list_open[-1] == '<':
                list_open.pop(-1)

        list_open.reverse()
        line_score = 0
        for symbol in list_open:
            if symbol == '(':
                line_score = line_score * 5 + 1
            elif symbol == '[':
                line_score = line_score * 5 + 2
            elif symbol == '{':
                line_score = line_score * 5 + 3
            elif symbol == '<':
                line_score = line_score * 5 + 4

        score.append(line_score)

    score.sort()
    return score[len(score) // 2]


if __name__ == '__main__':
    main()
