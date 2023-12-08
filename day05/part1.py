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


def parse_garden(garden_desc: list[str]) -> tuple[list[int], dict[str, Map]]:
    seeds = list(map(int, garden_desc[0].split(': ')[1].split()))
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
    return seeds, maps

def seed_to_location(seed: int, maps: dict[str, Map]) -> int:
    entity, x = 'seed', seed
    while entity != 'location':
        entity, x = maps[entity].target, maps[entity].convert(x)
    return x

def main():
    garden = library.read_input(5)
    seeds, maps = parse_garden(garden)
    print(min(seed_to_location(s, maps) for s in seeds))

if __name__ == "__main__":
    main()