import sys
from dataclasses import dataclass
from itertools import count


sys.path.append('../..')
from myFunctions import my_input_list  # noqa E402


def main():
    aoc_input = my_input_list("input.txt")

    print(part_one(aoc_input.copy()))
    print(part_two(aoc_input.copy()))


def part_one(aoc_input) -> int:
    # collect blueprints
    blueprints = []
    for blueprint in aoc_input:
        assert isinstance(blueprint, str)
        robots = []
        for robot in blueprint.split('.')[:-1]:
            r_type, cost = robot.split('costs')
            if 'ore' in r_type:
                r_type = 'ore'
            elif 'clay' in r_type:
                r_type = 'clay'
            elif 'obsidian' in r_type:
                r_type = 'obsidian'
            elif 'geode' in r_type:
                r_type = 'geode'
            else:
                continue

            r_cost = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
            for resource in cost.split('and'):
                r_cost[resource.split()[1]] = int(resource.split()[0])

            robots.append(Robot(r_type, r_cost))
        blueprints.append(robots)

    # build blueprints
    quality_levels = []
    for blueprint in blueprints:
        assert isinstance(blueprint, list)
        factory = Factory(blueprint)
        for _ in range(24):
            factory.work()
        quality_levels.append(factory.get_quality_level())
    return sum(quality_levels)


def part_two(aoc_input) -> int:
    return -1


@dataclass
class Robot:
    type: str
    cost: dict  # {ore, clay, obsidian, geode}


class Factory:
    id = count(1)

    def __init__(self, blueprint: list) -> None:
        self.blueprint = blueprint
        self.resources = {'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0}
        self.robots = {'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0}
        self.in_production = ''
        self.id = next(Factory.id)

    def work(self) -> None:
        """Collect resource and build robot. Takes 1 minute."""
        # build robot, if enough resource available
        for robot in self.blueprint[::-1]:
            assert isinstance(robot, Robot)
            if '' in robot:
                pass
            elif all(self.resources[resource] >= robot.cost[resource] for resource in self.resources.keys()):
                self._build_robot(robot)

        # collect resources from robots in use
        for resource, value in self.robots.items():
            self.resources[resource] += value

        if self.in_production != '':
            self._finish_robot()

    def get_quality_level(self) -> int:
        """Returns the quality level of the blueprint."""
        return self.id * self.resources['geode']

    def _build_robot(self, robot: Robot) -> None:
        """Start building the specified robot.

        :param robot: Robot to build
        :return: None
        """
        for resource, value in robot.cost.items():
            self.resources[resource] -= value
        self.in_production = robot.type

    def _finish_robot(self) -> None:
        """Finish building the robot in production"""
        self.robots[self.in_production] += 1
        self.in_production = ''


if __name__ == '__main__':
    main()
