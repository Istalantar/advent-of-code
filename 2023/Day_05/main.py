import sys
from typing import Dict

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    # print(part_one(aoc_input))
    print(part_two(aoc_input))


def part_one(aoc_input) -> int:
    almanac = Almanac(aoc_input)
    return almanac.plant()


def part_two(aoc_input) -> int:
    almanac = Almanac(aoc_input, part=2)
    return almanac.reverse_plant()


class Almanac:
    def __init__(self, aoc_input: str, part: int = 1):
        self._maps: Dict[str: list] = {'seed-to-soil': [],
                                       'soil-to-fertilizer': [],
                                       'fertilizer-to-water': [],
                                       'water-to-light': [],
                                       'light-to-temperature': [],
                                       'temperature-to-humidity': [],
                                       'humidity-to-location': []}
        self._seeds = []
        self._locations = []
        seeds, *maps = aoc_input.split('\n\n')
        maps = list(map(str.strip, maps))
        self._get_seeds(seeds)
        if part == 2:
            self._seeds_part_2()
        self._get_map_info(maps)

    def _get_seeds(self, seeds: str):
        self._seeds = list(map(str.strip, seeds.split(':')[1].split()))
        self._seeds = list(map(int, self._seeds))

    def _seeds_part_2(self):
        """Modifies the seeds info for part 2 of the solution,
        where the info is seed ranges not single seeds"""
        all_seeds = []
        # TODO: improve, since this runs forever
        for start, length in zip(self._seeds[::2], self._seeds[1::2]):
            all_seeds += list(range(start, start + length))
        self._seeds = all_seeds

    def _get_map_info(self, maps: list):
        map_info: str
        for i, map_info in enumerate(maps):
            my_map = list(map(str.strip, (map_info.split('\n'))))
            map_name = my_map[0].split()[0]
            for seed_range in my_map[1:]:  # ignore headline of the map
                dst_start, src_start, range_length = list(map(int, seed_range.split()))
                map_entry = self._maps.get(map_name)
                map_entry.append((dst_start, src_start, range_length))

    def plant(self) -> int:
        for i, seed in enumerate(self._seeds):
            temp = seed
            for map_name in self._maps.keys():
                for dst, src, rng in self._maps[map_name]:
                    if src <= temp < src + rng:
                        diff = temp - src
                        temp = dst + diff
                        break
            self._locations.append(temp)
            # print(f'Progress: {int(i/len(self._seeds)*100)}%')
        return min(self._locations)

    def reverse_plant(self):
        # TODO: could a bottoms-up solution be possible?
        #  -> starting with lowest location and traversing the maps backwards to see if there is a matching seed
        pass


if __name__ == '__main__':
    main()
