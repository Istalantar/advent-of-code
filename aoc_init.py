import sys
from os import path, getcwd, makedirs
from shutil import copyfile

YEAR = 2022


def main(day: int):
    project_path = getcwd()
    my_path = path.join(project_path, f'{YEAR}', f'Day_{day:02}')

    if not path.exists(my_path):
        makedirs(my_path)
        copyfile(path.join(project_path, 'templates', 'main.py'), path.join(my_path, 'main.py'))
        copyfile(path.join(project_path, 'templates', 'test_main.py'), path.join(my_path, 'test_main.py'))
        open(path.join(my_path, 'example.txt'), 'w')

        print(f'{YEAR}/Day_{day:02} initialized')
    else:
        print(f'{YEAR}/Day_{day:02} already exists')


if __name__ == '__main__':
    main(int(sys.argv[1]))
