import sys

sys.path.append('../..')
from myFunctions import my_input_string, my_input_list  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    print(part_one(aoc_input))
    print(part_two(aoc_input))


def part_one(aoc_input) -> int:
    my_map, my_path = aoc_input.split('\n\n')
    assert isinstance(my_map, str) and isinstance(my_path, str)
    board = Board(my_map, my_path)
    board.follow_path()

    return 1000 * board.position[1] + 4 * board.position[0] + board.facing


def part_two(aoc_input) -> int:
    return -1


class Board:
    def __init__(self, raw_map: str, path: str):
        self.board = self._create_board(raw_map)
        self.path = path.replace('R', ' R ').replace('L', ' L ').strip()  # add space to use it for split
        self.position = (1, 1)  # top left = (x, y) = (1, 1)
        self.facing = 0  # 0 = right, 1 = down, 2 = left, 3 = up
        self._find_start()

    @staticmethod
    def _create_board(raw_map: str) -> dict:
        board = {}
        for y, line in enumerate(raw_map.split('\n')):
            for x, char in enumerate(line):
                board[(x + 1, y + 1)] = char
        return board

    def _find_start(self):
        """First open tile in first row is starting point"""
        keys = sorted([key for key in self.board.keys() if key[1] == 1])
        for key in keys:
            if self.board[key] == '.':
                self.position = key
                return

    def follow_path(self):
        for step in self.path.split():
            if step == 'L':
                self.facing = self.facing - 1 if self.facing > 0 else 3
            elif step == 'R':
                self.facing = self.facing + 1 if self.facing < 3 else 0
            elif step.isnumeric():
                for _ in range(int(step)):
                    next_tile = self._next_tile()
                    if next_tile == (None, None):
                        break
                    else:
                        self.position = next_tile
            else:
                raise Exception('Unexpected step.')

    def _next_tile(self) -> tuple:
        """Gets the coordinates of the next tile when walking forward, inclunding a wrap around

        :return: Returns the coordinates of the next step as tuple. Or a None tuple, if the next step is a wall.
        """
        step = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
        next_step = tuple(map(sum, zip(self.position, step[self.facing])))

        if next_step in self.board.keys() and self.board[next_step] == '.':
            return next_step
        elif next_step in self.board.keys() and self.board[next_step] == '#':
            return None, None
        elif next_step not in self.board.keys() or self.board[next_step] == ' ':  # edge of board reached
            # collect next possible coordinates depending on facing
            coords = []
            if self.facing == 0:  # right
                coords = sorted([coord for coord in self.board.keys()
                                 if coord[1] == self.position[1] and coord[0] < self.position[0]])
            elif self.facing == 1:  # down
                coords = sorted([coord for coord in self.board.keys()
                                 if coord[0] == self.position[0] and coord[1] < self.position[1]])
            elif self.facing == 2:  # left
                # list sorted reversed, because search must be from right to left
                coords = sorted([coord for coord in self.board.keys()
                                 if coord[1] == self.position[1] and coord[0] > self.position[0]],
                                reverse=True)
            elif self.facing == 3:  # up
                # list sorted reversed, because search must be from bottom to top
                coords = sorted([coord for coord in self.board.keys()
                                 if coord[0] == self.position[0] and coord[1] > self.position[1]],
                                reverse=True)

            for coord in coords:
                if self.board[coord] == ' ':
                    continue
                elif self.board[coord] == '.':
                    return coord
                elif self.board[coord] == '#':
                    return None, None

        raise Exception('Unexpected next step')


if __name__ == '__main__':
    main()
