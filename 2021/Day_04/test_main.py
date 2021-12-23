from unittest import TestCase
from main import part_one, part_two


class TestExample(TestCase):
    def setUp(self) -> None:
        with open('example.txt', 'r') as file:
            file_content = file.read()
        self.content = file_content.split('\n\n')

    def test_part_one(self):
        self.assertEqual(part_one(self.content), 4512)

    def test_part_two(self):
        self.assertEqual(part_two(self.content), 1924)
