import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    caves = set(sum([line.split('-') for line in content], []))
    caves_dict = {}

    # get all caves with adjacent caves -> {'cave': ['adj1', 'adj2', ...]}
    for cave in caves:
        connected_caves = []
        for line in content:
            if cave + '-' in line or '-' + cave in line:
                if (temp := str(line).replace(cave, '').replace('-', '')) != 'start':
                    connected_caves.append(temp)
        caves_dict[cave] = connected_caves

    # find not allowed caves, e.g. small cave, which would need to be visited twice
    not_allowed_caves = []
    for key, val in caves_dict.copy().items():
        if len(val) <= 1 and val[0].islower():
            not_allowed_caves.append(key)
            caves_dict.pop(key)

    # remove not allowed caves
    for key, val in caves_dict.copy().items():
        for cave in not_allowed_caves:
            val.remove(cave) if cave in val else False

    # get unique ways
    visited = []
    output_list = []
    output = ['start']
    trace('start', output_list, output, visited, caves_dict)

    return len(output_list)


def part_two(content) -> int:
    caves = set(sum([line.split('-') for line in content], []))
    caves_dict = {}

    # get all caves with adjacent caves -> {'cave': ['adj1', 'adj2', ...]}
    for cave in caves:
        connected_caves = []
        for line in content:
            if cave + '-' in line or '-' + cave in line:
                if (temp := str(line).replace(cave, '').replace('-', '')) != 'start':
                    connected_caves.append(temp)
        caves_dict[cave] = connected_caves

    # get unique ways
    visited = []
    output_list = []
    output = ['start']
    trace2('start', output_list, output, visited, caves_dict)

    return len(output_list)


def trace(node, output_list, output, visited, graph):
    if node == 'end':
        output_list.append(output.copy())

    for cave in graph[node]:
        if (cave not in visited or cave.isupper()) and 'end' not in output:
            visited.append(cave) if cave.islower() else False
            output.append(cave)
            trace(cave, output_list, output, visited, graph)
            popped = output.pop(-1) if output else False
            if popped in visited:
                visited.remove(popped)


def trace2(node, output_list, output, visited, graph):
    is_small_visited_twice = False
    if node == 'end':
        output_list.append(output.copy())

    for cave in graph[node]:
        # if small cave only once in output list, then it can be visited again
        for s_cave in output:
            if s_cave != 'end' and s_cave.islower() and output.count(s_cave) > 1:
                is_small_visited_twice = True

        if ((cave not in visited or cave.isupper()) or not is_small_visited_twice) and 'end' not in output:
            visited.append(cave) if cave.islower() else False
            output.append(cave)
            trace2(cave, output_list, output, visited, graph)
            popped = output.pop(-1) if output else False
            if popped in visited:
                visited.remove(popped)


if __name__ == '__main__':
    main()
