import sys
import queue

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    start, end = get_start_end(aoc_input)
    area = [[ord(i) for i in row] for row in aoc_input]
    area[start[1]][start[0]] = ord('a')
    area[end[1]][end[0]] = ord('z')
    graph = get_graph(area)
    for node_k, node_v in graph.items():
        for neighbour_k, neighbour_v in node_v.items():
            if neighbour_v > 1:
                node_v[neighbour_k] = float('inf')
            else:
                node_v[neighbour_k] = 1

    path, dist = dijkstra(graph, start, end)
    return len(path) - 1


def part_two(aoc_input) -> int:
    return -1


def dijkstra(graph, src, dst):
    distances = {v: float('inf') for v in graph}
    distances[src] = 0
    predecessor = {node: None for node in graph}
    q = queue.PriorityQueue()
    q.put((0, src))  # first item in queue

    while len(q.queue) != 0:  # Pop node with smallest distance
        distance, node = q.get()

        # Update distances of neighbors
        for neighbor, weight in graph[node].items():
            new_distance = distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessor[neighbor] = node
                q.put((new_distance, neighbor))

    # Return the shortest path and its distance
    path = []
    current = dst
    while current is not None:
        path.append(current)
        current = predecessor[current]
    return path[::-1], distances[dst]


def get_graph(area) -> dict:
    """
    :param area: 2d list of all heights}
    :return: dictionary of all pillars with their height difference
    """
    graph = {}
    row_max = len(area)
    col_max = len(area[0])

    for y in range(row_max):
        for x in range(col_max):
            graph[(x, y)] = {}
            if y > 0:
                graph[(x, y)][(x, y - 1)] = abs(area[y][x] - area[y - 1][x])
            if x < col_max - 1:
                graph[(x, y)][(x + 1, y)] = abs(area[y][x] - area[y][x + 1])
            if y < row_max - 1:
                graph[(x, y)][(x, y + 1)] = abs(area[y][x] - area[y + 1][x])
            if x > 0:
                graph[(x, y)][(x - 1, y)] = abs(area[y][x] - area[y][x - 1])

    return graph


def get_start_end(heightmap) -> tuple[tuple, tuple]:
    start = end = None
    for y, row in enumerate(heightmap):
        for x, val in enumerate(row):
            if val == 'S':
                start = (x, y)
            elif val == 'E':
                end = (x, y)
            elif start is not None and end is not None:
                return start, end


if __name__ == '__main__':
    main()
