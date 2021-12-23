class Bag:
    def __init__(self, rule):
        self.full_rule = str(rule)
        self.rule = None
        self.rule_list = []
        self.name = str()  # name of the bag
        self.total_bags_count = 0  # count of all bags within this bag
        self.__get_name()
        self.__get_rule()
        self.__get_total_bags_count()

    def __repr__(self):
        return self.name

    def __get_name(self):
        # name is from beginning to second white space
        self.name = self.full_rule[:self.full_rule.find(' ', self.full_rule.find(' ') + 1)]

    def __get_rule(self):
        """
        sets 'rule' as string which starts with the word or number after 'contain'
        and creates a list of dictionaries of rules
        """
        temp = self.full_rule[self.full_rule.find('contain'):]
        self.rule = temp[temp.find(' ') + 1:]
        if 'no ' not in self.rule:
            rules = [x.strip() for x in self.rule.split(',')]
            for rule in rules:
                temp = rule.split(' ')
                self.rule_list.append({'name': f'{temp[1]} {temp[2]}', 'amount': int(temp[0])})

    def __get_total_bags_count(self):
        for x in self.rule.split(' '):
            if x.isnumeric():
                self.total_bags_count += int(x)


def find_part_one_result(bags) -> int:
    return remove_bag_with_rule(bags, 'shiny gold')


def remove_bag_with_rule(bags, bag_rule):
    bags_removed = 0

    for bag in bags.copy():
        if bag_rule in bag.rule:
            try:
                bags.remove(bag)
                bags_removed = bags_removed + 1 + remove_bag_with_rule(bags, bag.name)
            except ValueError:
                print(f'ValueError: Bag name = {bag.name}, Bag rule = {bag.rule}')

    return bags_removed


def find_part_two_result(bags, bag_name) -> int:
    bag_sum = 0

    for bag in bags.copy():
        if bag_name in bag.name:
            bag_sum += bag.total_bags_count
            for x in bag.rule_list:
                bag_sum += x['amount'] * find_part_two_result(bags, x['name'])

    return bag_sum


def main():
    with open("input.txt", 'r') as file:
        content = file.read().splitlines()

    all_bags = []

    for rule in content:
        all_bags.append(Bag(rule))

    print(f"Part One: {find_part_one_result(all_bags.copy())}")
    print(f"Part Two: {find_part_two_result(all_bags.copy(), 'shiny gold')}")


main()
