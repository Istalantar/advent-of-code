import sys
import copy
import queue

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    content = my_input_list("input.txt")

    print(part_one(content))
    print(part_two(content))
    print('2791 is not the correct answer!')


def part_one(content) -> int:
    max_y = len(content)
    max_x = len(content[0])
    cave = [[int(i) for i in row] for row in content]

    risk_graph = []
    nodes = set()
    for y in range(max_y):
        row = []
        for x in range(max_x):
            row.append(float('inf'))
            nodes.add((x, y))
        risk_graph.append(row)

    risk_graph[0][0] = 0  # starting point
    nodes = [(x, y) for x in range(len(cave[0])) for y in range(len(cave))]

    # create edges (risk from point one to point two
    # {((x1, y1), (x2, y2)): risk}
    edges = get_edges(cave, len(cave[0]), len(cave))

    risk_graph = dijkstra(nodes, edges)

    return risk_graph[(len(cave[0]) - 1, len(cave) - 1)]


def part_two(content) -> int:
    max_y = len(content)
    max_x = len(content[0])
    cave = [[int(i) for i in row] for row in content]

    risk_graph = []
    for y in range(max_y):
        row = []
        for x in range(max_x):
            row.append(float('inf'))
        risk_graph.append(row)

    # make 5 times bigger
    risk_graph = [row * 5 for row in risk_graph]

    # region adjust risk in x direction
    cave = [row * 5 for row in cave]
    for y in range(len(cave)):
        i = 0
        for x in range(len(cave[0])):
            cave[y][x] = cave[y][x] + i
            cave[y][x] -= 9 if cave[y][x] > 9 else 0
            i += 1 if x % max_x == 9 else 0
    # endregion

    # region adjust risk in y direction
    temp_cave = copy.deepcopy(cave)
    temp_risk_grap = copy.deepcopy(risk_graph)
    for _ in range(4):
        cave += copy.deepcopy(temp_cave)
        risk_graph += copy.deepcopy(temp_risk_grap)

    risk_graph[0][0] = 0  # starting point

    i = 0
    for y in range(len(cave)):
        for x in range(len(cave[0])):
            cave[y][x] = cave[y][x] + i
            cave[y][x] -= 9 if cave[y][x] > 9 else 0
        i += 1 if y % max_y == 9 else 0
    # endregion

    nodes = [(x, y) for x in range(len(cave[0])) for y in range(len(cave))]

    # create edges (risk from point one to point two
    # {((x1, y1), (x2, y2)): risk}
    edges = get_edges(cave, len(cave[0]), len(cave))

    risk_graph = dijkstra(nodes, edges)
    return risk_graph[(len(cave[0]) - 1, len(cave) - 1)]


def dijkstra(nodes, edges):
    risk_graph = {v: float('inf') for v in nodes}
    risk_graph[(0, 0)] = 0
    q = queue.PriorityQueue()

    adjacent_nodes = {v: {} for v in nodes}
    for (x, y), risk in edges.items():
        adjacent_nodes[x][y] = risk

    temporary_nodes = [v for v in nodes]
    q.put((0, (0, 0)))  # first item in queue
    while len(temporary_nodes) > 0:
        risk, u = q.get()
        if u not in temporary_nodes:
            continue
        temporary_nodes.remove(u)

        for v, risk in adjacent_nodes[u].items():
            risk_graph[v] = min(risk_graph[v], risk_graph[u] + risk)
            if v in temporary_nodes:
                q.put((risk_graph[v], v))

        print(len(temporary_nodes))

    return risk_graph


def get_edges(cave, row_size, col_size) -> dict:
    """
    :param cave: 2d list of all risks}
    :param row_size: size of a row
    :param col_size: size of a column
    :return: set of all edges with their risk
    """
    edges = {}

    for y in range(col_size):
        is_top_border = True if y == 0 else False
        is_bottom_border = True if y + 1 == col_size else False
        for x in range(row_size):
            is_right_border = True if x + 1 == row_size else False
            is_left_border = True if x == 0 else False

            if not is_top_border:
                edges[((x, y), (x, y - 1))] = cave[y - 1][x]
            if not is_right_border:
                edges[((x, y), (x + 1, y))] = cave[y][x + 1]
            if not is_bottom_border:
                edges[((x, y), (x, y + 1))] = cave[y + 1][x]
            if not is_left_border:
                edges[((x, y), (x - 1, y))] = cave[y][x - 1]

    return edges


if __name__ == '__main__':
    main()
