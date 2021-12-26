import sys
import itertools

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


class DiracDice:
    def __init__(self, p1_pos, p2_pos):
        self.die = itertools.count(1)
        self.p1_pos = p1_pos
        self.p2_pos = p2_pos
        self.p1_pts = 0  # Points player 1
        self.p2_pts = 0  # Points player 2
        self.roll_count = 0

    def roll(self) -> int:
        self.roll_count += 1
        val = next(self.die)

        if val == 100:
            self.die = itertools.count(1)

        return val

    def p1_move(self, moves):
        self.p1_pos += moves % 10
        if self.p1_pos > 10:
            self.p1_pos -= 10
        self.p1_pts += self.p1_pos
        return self.p1_pts

    def p2_move(self, moves):
        self.p2_pos += moves % 10
        if self.p2_pos > 10:
            self.p2_pos -= 10
        self.p2_pts += self.p2_pos
        return self.p2_pts


def main():
    print(part_one(3, 4))
    print(part_two())


def part_one(p1_start, p2_start) -> int:
    game = DiracDice(p1_start, p2_start)  # Starting positions from input file

    while True:
        # Player 1 turn
        move_cnt = sum([game.roll(), game.roll(), game.roll()])
        if game.p1_move(move_cnt) >= 1000:
            break

        # Player 2 turn
        move_cnt = sum([game.roll(), game.roll(), game.roll()])
        if game.p2_move(move_cnt) >= 1000:
            break

    return min(game.p1_pts, game.p2_pts) * game.roll_count


def part_two() -> int:
    return 0


if __name__ == '__main__':
    main()
