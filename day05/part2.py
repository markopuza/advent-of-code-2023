from common import library

class Map:
    def __init__(self, source: str, target: str, values: tuple[int]) -> None:
        self.source = source
        self.target = target
        self.values = values

    def __str__(self):
        return f'Map {self.source}-to-{self.target}: {", ".join(map(str, self.values))}'
    
    def __repr__(self):
        return self.__str__()
    
    def convert(self, x: int) -> int:
        for dest, range, length in self.values:
            if x >= range and x - range < length:
                return dest + x - range
        return x

    def convert_range(self, seed_range: tuple[int]) -> list[tuple[int]]:
        x, y = seed_range
        endpoints = set([x, y])
        for _, r, l in self.values:
            if x < r <= y:
                endpoints.add(r)
                endpoints.add(r - 1)
            if x <= r + l - 1 < y:
                endpoints.add(r + l - 1)
                endpoints.add(r + l)
        intervals = [(a, b) for a, b in zip(sorted(endpoints), sorted(endpoints)[1:])][0::2]
        return [(self.convert(a), self.convert(b)) for a, b in intervals]



def parse_garden(garden_desc: list[str]) -> tuple[list[tuple[int]], dict[str, Map]]:
    seeds = list(map(int, garden_desc[0].split(': ')[1].split()))
    seed_ranges = [(x, x + y - 1) for x, y in zip(seeds, seeds[1:])][0::2]
    maps = {}
    source, target, curr_values = '', '', []
    for row in garden_desc[1:]:
        if row == '':
            if curr_values:
                maps[source] = Map(source, target, curr_values)
            source, target, curr_values = '', '', []
        elif ' map:' in row:
            source = row.split('-to-')[0]
            target = row.split('-to-')[1].split()[0]
        else:
            curr_values.append(tuple(map(int, row.split())))
    maps[source] = Map(source, target, curr_values)
    return seed_ranges, maps

def seed_range_to_location_ranges(seed_ranges: list[tuple[int]], maps: dict[str, Map]) -> list[tuple[int]]:
    entity, ranges = 'seed', seed_ranges
    while entity != 'location':
        new_ranges = []
        for r in ranges:
            new_ranges.extend(maps[entity].convert_range(r))
        entity, ranges = maps[entity].target, new_ranges
    return ranges 

def main():
    garden = library.read_input(5)
    seed_ranges, maps = parse_garden(garden)
    location_ranges = seed_range_to_location_ranges(seed_ranges, maps)
    print(min(a for a, _ in location_ranges if a))

if __name__ == "__main__":
    main()