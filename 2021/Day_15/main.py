import sys
import copy

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))


# noinspection PyTypeChecker
def part_one(content) -> int:
    max_y = len(content)
    max_x = len(content[0])
    cave = [[int(i) for i in row] for row in content]

    risk_graph = []
    unvisited = set()
    for y in range(max_y):
        row = []
        for x in range(max_x):
            row.append(None)
            unvisited.add((x, y))
        risk_graph.append(row)

    risk_graph[0][0] = 0  # starting point

    my_dijkstra(cave, risk_graph, unvisited)

    return risk_graph[max_y - 1][max_x - 1]


# noinspection PyTypeChecker
def part_two(content) -> int:
    max_y = len(content) - 1
    max_x = len(content[0]) - 1
    cave = [[int(i) for i in row] for row in content]

    risk_graph = []
    unvisited = set()
    for y in range(max_y + 1):
        row = []
        for x in range(max_x + 1):
            row.append(None)
        risk_graph.append(row)

    # make 5 times bigger
    risk_graph = [row * 5 for row in risk_graph]

    # adjust risk in x direction
    cave = [row * 5 for row in cave]
    for y in range(len(cave)):
        i = 0
        for x in range(len(cave[0])):
            cave[y][x] = cave[y][x] + i
            cave[y][x] -= 9 if cave[y][x] > 9 else 0
            i += 1 if x % (max_x + 1) == 9 else 0

    # adjust risk in y direction
    temp_cave = copy.deepcopy(cave)
    temp_risk_grap = copy.deepcopy(risk_graph)
    for _ in range(4):
        cave += copy.deepcopy(temp_cave)
        risk_graph += copy.deepcopy(temp_risk_grap)

    i = 0
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            cave[y][x] = cave[y][x] + i
            cave[y][x] -= 9 if cave[y][x] > 9 else 0
        i += 1 if y % (max_y + 1) == 9 else 0

    unvisited = {(x, y) for x in range(len(cave[0])) for y in range(len(cave))}

    # run path search
    risk_graph[0][0] = 0  # starting point
    my_dijkstra(cave, risk_graph, unvisited)

    return risk_graph[len(cave) - 1][len(cave[0]) - 1]


def my_dijkstra(cave, risk_graph, unvisited):
    while unvisited:
        for y, row in enumerate(risk_graph):
            for x, risk in enumerate(row):
                # look into right neighbour
                if not x + 1 >= len(row):
                    if risk_graph[y][x + 1] is None:
                        risk_graph[y][x + 1] = risk + cave[y][x + 1]
                    elif risk_graph[y][x + 1] > risk + cave[y][x + 1]:
                        risk_graph[y][x + 1] = risk + cave[y][x + 1]

                # look into below neighbour
                if not y + 1 >= len(risk_graph):
                    if risk_graph[y + 1][x] is None:
                        risk_graph[y + 1][x] = risk + cave[y + 1][x]
                    elif risk_graph[y + 1][x] > risk + cave[y + 1][x]:
                        risk_graph[y + 1][x] = risk + cave[y + 1][x]

                unvisited.remove((x, y))


if __name__ == '__main__':
    main()
