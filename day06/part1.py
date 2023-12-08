from common import library
from functools import reduce
import operator

Race = tuple[int]

def parse_races(races_desc: list[str]) -> list[Race]:
    times = list(map(int, [x for x in races_desc[0].split(':')[1].split() if x]))
    distances = list(map(int, [x for x in races_desc[1].split(':')[1].split() if x]))
    return list(zip(times, distances))

def ways_to_win(race: Race) -> int:
    ways = 0
    T, D = race
    for pressed in range(T + 1):
        if pressed * (T - pressed) > D:
            ways += 1
    return ways

def main():
    races = parse_races(library.read_input(6))
    print(reduce(operator.mul, [ways_to_win(r) for r in races], 1))

if __name__ == "__main__":
    main()