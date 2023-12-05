import sys

sys.path.append('../..')
from myFunctions import my_input_string  # noqa E402


def main():
    aoc_input = my_input_string("input.txt")

    print(part_one(aoc_input))
    print(part_two(aoc_input))


def part_one(aoc_input) -> int:
    almanac = Almanac(aoc_input)
    return almanac.plant()


def part_two(aoc_input) -> int:
    return -1


class Almanac:
    def __init__(self, aoc_input: str):
        _seed_to_soil = {}
        _soil_to_fertilizer = {}
        _fertilizer_to_water = {}
        _water_to_light = {}
        _light_to_temperature = {}
        _temperature_to_humidity = {}
        _humidity_to_location = {}
        # maps as list in the order the need to be applied
        self._maps = [_seed_to_soil,  # 0
                      _soil_to_fertilizer,  # 1
                      _fertilizer_to_water,  # 2
                      _water_to_light,  # 3
                      _light_to_temperature,  # 4
                      _temperature_to_humidity,  # 5
                      _humidity_to_location]  # 6
        self._seeds = []
        seeds, *maps = aoc_input.split('\n\n')
        self._get_seeds(seeds)
        self._create_maps(maps)

    def _get_seeds(self, seeds: str):
        self.seeds = list(map(str.strip, seeds.split(':')[1].split()))
        self.seeds = list(map(int, self.seeds))

    def _create_maps(self, maps: list):
        map_info: str
        for i, map_info in enumerate(maps):
            print(f'map nr: {i}')
            ranges = map_info.split('\n')
            for seed_range in ranges[1:]:  # ignore headline of the map
                dst_start, src_start, range_length = list(map(int, list(map(str.strip, seed_range.split()))))
                for destination, source in zip(range(dst_start, dst_start + range_length),
                                               range(src_start, src_start + range_length)):
                    self._maps[i][source] = destination

    def plant(self) -> int:
        """Plants everything and returns location"""
        # get soil
        soils = []
        for seed in self.seeds:
            soils.append(self._maps[0].get(seed, seed))
        print('seeds done')

        # get fertilizer
        fertilizers = []
        for soil in soils:
            fertilizers.append(self._maps[1].get(soil, soil))
        print('soil done')

        # get water
        waters = []
        for fertilizer in fertilizers:
            waters.append(self._maps[2].get(fertilizer, fertilizer))
        print('fertilizer done')

        # get light
        lights = []
        for water in waters:
            lights.append(self._maps[3].get(water, water))
        print('water done')

        # get temperature
        temperatures = []
        for light in lights:
            temperatures.append(self._maps[4].get(light, light))
        print('light done')

        # get humidity
        humidities = []
        for temperature in temperatures:
            humidities.append(self._maps[5].get(temperature, temperature))
        print('temperature done')

        # get location
        locations = []
        for humidity in humidities:
            locations.append(self._maps[6].get(humidity, humidity))
        print('location done')

        return min(locations)


if __name__ == '__main__':
    main()
