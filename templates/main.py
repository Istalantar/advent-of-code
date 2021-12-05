from myFunctions import my_input
from unittest import TestCase


class TestExample(TestCase):
    def setUp(self) -> None:
        self.content = my_input("example.txt")

    def test_part_one(self):
        self.assertEqual(part_one(self.content), -1)

    def test_part_two(self):
        self.assertEqual(part_two(self.content), -1)


def main():
    content = my_input("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    res = 0
    return res


def part_two(content) -> int:
    res = 0
    return res


if __name__ == '__main__':
    main()
