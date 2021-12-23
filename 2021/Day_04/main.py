import itertools


class Bingo:
    bingo_id = itertools.count()

    def __init__(self, board=str()):
        self.id = next(self.bingo_id)
        self.board = []  # 5x5 grid
        self.marked_board = []
        self.row_match_count = [0, 0, 0, 0, 0]
        self.col_match_count = [0, 0, 0, 0, 0]
        self.draw_count = 0
        self.drawn_number = 0
        self.final_score = 0
        self.has_row_won = False
        self.has_col_won = False

        self.marked_board = [[False for x in range(5)] for y in range(5)]
        board_row = board.splitlines()
        for line in board_row:
            board_val = line.split()
            self.board.append([board_val[i].strip() for i, value in enumerate(board_val)])

    def __repr__(self):
        return f"Board ID: {self.id}, Final Score: {self.final_score}"

    def find_match(self, number=str()) -> bool:
        """
        Finds matching number on board
        :param number: Number to find
        :return: True if board has one, else False
        """
        self.draw_count += 1
        self.drawn_number = number

        # see if number in bingo and track column / row
        for row_index, my_row in enumerate(self.board):
            for col_index, my_value in enumerate(my_row):
                if my_value == number:
                    self.marked_board[row_index][col_index] = True
                    self.row_match_count[row_index] += 1
                    self.col_match_count[col_index] += 1

        # check if bingo is won
        my_sum = 0
        for i in range(5):
            if self.row_match_count[i] == 5:
                for j in range(5):
                    my_sum += int(self.board[i][j])
                self.has_row_won = True
                self.__get_final_score()
                return True
            elif self.col_match_count[i] == 5:
                my_sum = 0
                for j in range(5):
                    my_sum += int(self.board[j][i])
                self.has_col_won = True
                self.__get_final_score()
                return True

        return False

    def __get_final_score(self):
        res = 0
        for y, my_row in enumerate(self.marked_board):
            for x, value in enumerate(my_row):
                if not value:
                    res += int(self.board[y][x])
        self.final_score = int(res) * int(self.drawn_number)


def main():
    with open('input.txt', 'r') as file:
        file_content = file.read()

    content = file_content.split('\n\n')

    print(part_one(content.copy()))
    print(part_two(content.copy()))


def part_one(content) -> int:
    numbers = content.pop(0)

    boards = [Bingo(board) for board in content]
    boards_won = []

    for number in numbers.split(','):
        for board in boards.copy():
            if board.find_match(number):
                boards_won.append(board)
                boards.remove(board)

    return boards_won[0].final_score


def part_two(content) -> int:
    numbers = content.pop(0)

    boards = [Bingo(board) for board in content]
    boards_won = []

    for number in numbers.split(','):
        for board in boards.copy():
            if board.find_match(number):
                boards_won.append(board)
                boards.remove(board)

    return boards_won[-1].final_score


if __name__ == '__main__':
    main()
