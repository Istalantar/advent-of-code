import sys
from enum import Enum

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    hands = []
    for hand_and_bid in aoc_input:
        cards, bid = hand_and_bid.split()
        hands.append(CamelHand(cards, int(bid)))

    hands.sort()  # sort from lowest to highest hand
    total_winnings = 0
    hand: CamelHand
    for i, hand in enumerate(hands):
        total_winnings += (i + 1) * hand.bid

    return total_winnings


def part_two(aoc_input) -> int:
    return -1


class HandType(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

    def __gt__(self, other):
        return self.value > other.value


class CamelHand:
    LABEL_VALUE = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
                   '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    def __init__(self, hand: str, bid: int):
        self.hand = hand
        self.bid = bid
        self.hand_type: HandType = self._get_hand_type()

    def _get_hand_type(self) -> HandType:
        label_count = len(set(self.hand))
        if label_count == 1:
            # can only be five of a kind
            return HandType.FIVE_OF_A_KIND
        elif label_count == 2:
            # can be four of a kind or a full house
            label_1, label_2 = set(self.hand)
            if self.hand.count(label_1) == 4 or self.hand.count(label_1) == 1:
                return HandType.FOUR_OF_A_KIND
            elif self.hand.count(label_1) == 3 or self.hand.count(label_1) == 2:
                return HandType.FULL_HOUSE
            else:
                raise ValueError(f'Impossible hand found: {self.hand=}')
        elif label_count == 3:
            # can be three of a kind or two pair
            label_1, label_2, label_3 = set(self.hand)
            if self.hand.count(label_1) == 3 or self.hand.count(label_2) == 3 or self.hand.count(label_3) == 3:
                return HandType.THREE_OF_A_KIND
            else:
                return HandType.TWO_PAIR
        elif label_count == 4:
            # can only be one pair
            return HandType.ONE_PAIR
        elif label_count == 5:
            # can only be high card
            return HandType.HIGH_CARD
        else:
            raise ValueError(f'Invalid label count: {label_count=}, {self.hand=}')

    def __gt__(self, other) -> bool:
        if self.hand_type > other.hand_type:
            # hand one is stronger
            return True
        elif self.hand_type < other.hand_type:
            # hand two is stronger
            return False
        else:
            # both hand have the same strength
            for a, b in zip(self.hand, other.hand):
                val_a = self.LABEL_VALUE[a]
                val_b = self.LABEL_VALUE[b]
                if val_a > val_b:
                    return True
                elif val_a < val_b:
                    return False
        raise ValueError(f'Bigger hand could not be determined: hand 1 = {self.hand}, hand 2 = {other.hand}')


if __name__ == '__main__':
    main()
