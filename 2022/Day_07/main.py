import sys

sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


class FileSystem:
    def __init__(self, info):
        self.directories = {'/'}
        self.dir_size = {'/': 0}
        self.cwd = '/'
        self.max_space = 0
        self.min_space_needed = 0
        self._build_file_system(info)

    def _build_file_system(self, info):
        for line in info:
            if line.startswith('$'):
                self._execute_command(line[2:])
            else:
                if self.dir_size.get(self.cwd) is None:
                    self.dir_size[self.cwd] = 0
                self._list_dir(line)

    def _execute_command(self, cmd):
        if 'cd' in cmd:
            if '..' in cmd:
                self.cwd = '/'.join(self.cwd.split('/')[:-1])
            elif '/' in cmd:
                self.cwd = '/'
            else:
                # does the code want to enter dirs which don't exist?
                self.cwd += cmd.split()[1] + '/'
        elif 'ls' in cmd:
            # nothing to do here
            pass

    def _list_dir(self, info):
        if info.startswith('dir'):
            self.directories.add(self.cwd + info.split()[-1] + '/')
        else:
            file_size = int(info.split()[0])
            self.dir_size[self.cwd] += file_size
            # iterate through all parent directories and add file size
            parent_dirs_count = len(self.cwd.split('/')) - 2
            for i in range(-parent_dirs_count - 1, 0 - 1):
                self.dir_size['/'.join(self.cwd.split('/')[:i]) + '/'] += file_size

    def list_dirs(self, min_size: int) -> dict:
        """List all directories with a minimum size of {min_size}"""
        my_dict = {}
        for key, value in self.dir_size.items():
            if value > min_size:
                my_dict[key] = value
        return my_dict

    def get_fs_size(self) -> int:
        return self.dir_size['/']


def part_one(aoc_input) -> int:
    f = FileSystem(aoc_input)
    bla = [val if val <= 100000 else 0 for val in f.dir_size.values()]
    return sum(bla)


def part_two(aoc_input) -> int:
    f = FileSystem(aoc_input)
    f.max_space = 70_000_000
    f.min_space_needed = 30_000_000
    available_space = f.max_space - f.get_fs_size()
    dirs = f.list_dirs(f.min_space_needed - available_space)
    return min(dirs.values())


if __name__ == '__main__':
    main()
