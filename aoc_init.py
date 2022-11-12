import sys
from os import path, getcwd, makedirs
from shutil import copyfile

YEAR = 2019
MAIN_TEMPLATE_PATH = 'C:/Users/andre/Workspace/advent-of-code/templates/main.py'
TEST_TEMPLATE_PATH = 'C:/Users/andre/Workspace/advent-of-code/templates/test_main.py'


def main(day: int):
    my_path = path.join(getcwd(), f'{YEAR}', f'Day_{day:02}')

    if not path.exists(my_path):
        makedirs(my_path)
        copyfile(MAIN_TEMPLATE_PATH, path.join(my_path, 'main.py'))
        copyfile(TEST_TEMPLATE_PATH, path.join(my_path, 'test_main.py'))

        print(f'{YEAR}/Day_{day:02} initialized')
    else:
        print(f'{YEAR}/Day_{day:02} already exists')


if __name__ == '__main__':
    main(int(sys.argv[1]))
