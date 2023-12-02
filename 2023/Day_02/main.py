import sys
from typing import List
import math

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    sum_ids = 0
    cube_game = CubeGame()
    for game in aoc_input:
        game_id, drawn_cubes = list(map(str.strip, game.split(':')))
        game_id = int(game_id.split()[1])
        sum_ids += game_id if cube_game.evaluate_game(drawn_cubes) else 0

    return sum_ids


def part_two(aoc_input) -> int:
    sum_powers = 0
    cube_game = CubeGame()
    for game in aoc_input:
        _, drawn_cubes = list(map(str.strip, game.split(':')))
        sum_powers += cube_game.get_cube_power(drawn_cubes)

    return sum_powers


class CubeGame:
    def __init__(self):
        self.cube_limit = {'red': 12, 'green': 13, 'blue': 14}

    def evaluate_game(self, drawn_cubes: str) -> bool:
        """Evaluates if the game is possible or not.
        :param drawn_cubes: Information about the drwawn cubes
        :return: True if game is possible, False if not
        """
        cube_sets: List[str] = list(map(str.strip, drawn_cubes.split(';')))
        for cube_set in cube_sets:
            for cube in list(map(str.strip, cube_set.split(','))):
                number, color = cube.split()
                if int(number) > self.cube_limit[color]:
                    return False

        return True

    @staticmethod
    def get_cube_power(drawn_cubes: str) -> int:
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}
        cube_sets: List[str] = list(map(str.strip, drawn_cubes.split(';')))
        for cube_set in cube_sets:
            for cube in list(map(str.strip, cube_set.split(','))):
                number, color = cube.split()
                min_cubes[color] = max(min_cubes[color], int(number))

        return int(math.prod(min_cubes.values()))


if __name__ == '__main__':
    main()
