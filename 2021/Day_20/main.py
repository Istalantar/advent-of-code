import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    content = my_input_string("input.txt")

    print(part_one(content))
    print(part_two(content))


def part_one(content) -> int:
    algo, img_in = content.strip().split('\n\n')
    img_out = img_in
    
    for i in range(1, 3):  # image will be enhanced twice
        img_out = enhance(img_out, algo, i)

    return sum([True if char == '#' else False for char in img_out])


def part_two(content) -> int:
    return 0


def enhance(image: str, algo: str, enh_cnt: int) -> str:
    """    
    :param image: string representation of the image, with '#' = 1 and '.' = 0 
    :param algo: algorithm with which the image will be enhanced
    :param enh_cnt: number of enhancements to the original image (1 = first enhancement, etc.)
    :return: enhanced image
    """
    i_out = [list(row) for row in image.split('\n')]
    inf = ''

    if algo[0] == '#' and algo[-1] == '.':
        inf = '#' if enh_cnt % 2 == 0 else '.'
    elif algo[0] == '#' and algo[-1] == '#':
        inf = '#'
    elif algo[0] == '.':  # ininite outside will never be on, hence algo[-1] not needed
        inf = '.'

    # resize output image (two pixel bigger in each direction)
    i_out.insert(0, list(inf * len(i_out[0])))
    i_out.append(list(inf * len(i_out[0])))
    for i in range(len(i_out)):
        i_out[i] = [inf] + i_out[i] + [inf]

    # input image gets resized one more time because of grid needed for algorithm
    i_in = i_out.copy()
    i_in.insert(0, list(inf * len(i_in[0])))
    i_in.append(list(inf * len(i_in[0])))
    for i in range(len(i_in)):
        i_in[i] = [inf] + i_in[i] + [inf]

    # apply algorithm
    # for [0][0] in i_out following coordinates are needed from i_in
    # [0][0], [0][1], [0][2]
    # [1][0], [1][1], [1][2]
    # [2][0], [2][1], [2][2]
    # for [9][9] in i_out following coordinates are needed from i_in
    # [8][8], [8][9], [8][10]
    # [9][8], [9][9], [9][10]
    # [10][8], [10][9], [10][10]
    for i in range(1, len(i_out) + 1):
        for j in range(1, len(i_out[0]) + 1):
            y_out = i - 1
            x_out = j - 1
            idx = i_in[i - 1][j - 1:j + 2] + i_in[i][j - 1:j + 2] + i_in[i + 1][j - 1:j + 2]
            idx = int(''.join(idx).replace('.', '0').replace('#', '1'), 2)
            i_out[y_out][x_out] = algo[idx]

    return '\n'.join([''.join(row) for row in i_out])


if __name__ == '__main__':
    main()
