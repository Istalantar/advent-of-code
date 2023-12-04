import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    total_points = 0

    for line in aoc_input:
        card_name, card_info = list(map(str.strip, (line.split(':'))))
        winning_numbers, my_numbers = list(map(str.strip, (card_info.split('|'))))
        winning_numbers = list(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))
        card_points = 0
        is_first_number = True
        for number in my_numbers:
            if number in winning_numbers and is_first_number:
                is_first_number = False
                card_points = 1
            elif number in winning_numbers and not is_first_number:
                card_points *= 2
            else:
                pass
        total_points += card_points

    return total_points


def part_two(aoc_input) -> int:
    scratchcards = {i: 1 for i in range(1, len(aoc_input) + 1)}
    card_results = {}

    for key, card_count in scratchcards.items():
        card_name, card_info = list(map(str.strip, (aoc_input[key-1].split(':'))))
        card_id = int(card_name.split()[1])
        print(f'{card_id=}')
        matching_numbers = 0

        for _ in range(card_count):  # loop until all cards of that id are used up
            if card_id in card_results.keys():
                # wins in card are already known, so just take that value
                matching_numbers = card_results[card_id]
            else:
                # wins in card are not know, so evaluate
                winning_numbers, my_numbers = list(map(str.strip, (card_info.split('|'))))
                winning_numbers = list(map(int, winning_numbers.split()))
                my_numbers = list(map(int, my_numbers.split()))
                for number in my_numbers:
                    if number in winning_numbers:
                        matching_numbers += 1
                card_results[card_id] = matching_numbers

            # add copies of cards
            for j in range(card_id + 1, card_id + matching_numbers + 1):
                scratchcards[j] += 1

    return sum(scratchcards.values())


if __name__ == '__main__':
    main()
