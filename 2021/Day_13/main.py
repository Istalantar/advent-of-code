import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    content = my_input_string("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    x = []
    y = []
    manual = []
    coords, folds = content.split('\n\n')
    coords = coords.split('\n')
    folds = folds.split('\n')
    folds.pop(-1) if folds[-1] == '' else False

    # get all coordinates
    for line in coords:
        x.append(int(line.split(',')[0]))
        y.append(int(line.split(',')[1]))

    max_x = max(x) + 1
    max_y = max(y) + 1
    manual = [['.' for x in range(max_x)] for y in range(max_y)]
    for x, y in zip(x, y):
        manual[y][x] = '#'

    folded_manual = manual.copy()
    folds_count = 0
    for fold in folds:
        folds_count += 1
        fold_val = int(fold[fold.find('=') + 1:])

        if 'x' in fold:
            temp = []

            for y, row in enumerate(folded_manual):
                row.pop(fold_val)
                temp.append(list(map(lambda a: '#' if '#' in a[0] or '#' in a[1] else '.',
                                     zip(row[:fold_val], row[fold_val::][::-1]))))

            folded_manual = temp
        elif 'y' in fold:
            temp = []
            folded_manual.pop(fold_val)

            for i in range(fold_val):
                fold_temp = folded_manual[:fold_val], folded_manual[fold_val::][::-1]
                temp.append(list(map(lambda a: '#' if '#' in a[0] or '#' in a[1] else '.',
                                     zip(fold_temp[0][i], fold_temp[1][i]))))

            folded_manual = temp

        if folds_count == 1:
            break

    return sum(sum([[True if val == '#' else False for val in row] for row in folded_manual], []))


def part_two(content) -> int:
    x = []
    y = []
    manual = []
    coords, folds = content.split('\n\n')
    coords = coords.split('\n')
    folds = folds.split('\n')
    folds.pop(-1) if folds[-1] == '' else False

    # get all coordinates
    for line in coords:
        x.append(int(line.split(',')[0]))
        y.append(int(line.split(',')[1]))

    max_x = max(x) + 1
    max_y = max(y) + 1
    manual = [['.' for x in range(max_x)] for y in range(max_y)]
    for x, y in zip(x, y):
        manual[y][x] = '#'

    folded_manual = manual.copy()
    folds_count = 0
    instructions = 0
    for fold in folds:
        folds_count += 1
        fold_val = int(fold[fold.find('=') + 1:])

        if 'x' in fold:
            temp = []

            for y, row in enumerate(folded_manual):
                row.pop(fold_val)
                temp.append(list(map(lambda a: '#' if '#' in a[0] or '#' in a[1] else '.',
                                     zip(row[:fold_val], row[fold_val::][::-1]))))

            folded_manual = temp
        elif 'y' in fold:
            temp = []
            folded_manual.pop(fold_val)

            for i in range(fold_val):
                fold_temp = folded_manual[:fold_val], folded_manual[fold_val::][::-1]
                temp.append(list(map(lambda a: '#' if '#' in a[0] or '#' in a[1] else '.',
                                     zip(fold_temp[0][i], fold_temp[1][i]))))

            folded_manual = temp
        instructions += sum(sum([[True if val == '#' else False for val in row] for row in folded_manual], []))

    # get letters
    [print(line) for line in folded_manual]

    return 0


if __name__ == '__main__':
    main()
