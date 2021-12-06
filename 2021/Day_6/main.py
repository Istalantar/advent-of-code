import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


class Fish:
    def __init__(self, internal_timer: int):
        self.internal_timer = internal_timer

    def age_days(self, days) -> int:
        new_fish_timer = 0
        self.internal_timer -= 1

        if self.internal_timer < 0:
            new_fish_timer = 8
            self.internal_timer = 6

        return new_fish_timer


def main():
    content = my_input_string("input.txt")

    # print(part_one(content, 80))
    print(part_two(content, 256))


def part_one(content, days) -> int:
    school = []
    [school.append(Fish(int(num))) for num in content.split(',')]

    for i in range(days):
        new_school = school.copy()  # because I can't add fish to the list in the for loop
        for fish in school:
            new_fish = fish.age_days(1)
            if new_fish != 0:
                new_school.append(Fish(new_fish))
        school = new_school

    return len(school)


def part_two(content, days) -> int:
    school = {i: 0 for i in range(9)}  # initialize dictionary

    for num in content.split(','):  # fill dictionary with fish at day 1
        school[int(num)] += 1

    for i in range(days):
        new_fish = school[0]
        for j in range(9):
            if j == 6:
                school[j] = school[j+1] + new_fish
            elif j == 8:
                school[j] = new_fish
            else:
                school[j] = school[j+1]

    return sum(school.values())


if __name__ == '__main__':
    main()
