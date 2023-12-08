from common import library
import math

Race = tuple[int]

def parse_instructions(instructions_desc: list[str]) -> tuple[str, dict[str, tuple[str]]]:
    lrs = instructions_desc[0]
    map = {}
    for row in instructions_desc[2:]:
        map[row.split(' =')[0]] = (row.split('(')[1].split(',')[0], row.split(', ')[1].split(')')[0])
    return lrs, map

def steps_a_to_z(lrs: str, map: dict[str, tuple[str]], node: str):
    steps, curr = 0, node
    while curr[-1] != 'Z':
        curr = map[curr][0] if lrs[steps % len(lrs)] == 'L' else map[curr][1]
        steps += 1
    return steps

def main():
    lrs, map = parse_instructions(library.read_input(8))
    periods = [steps_a_to_z(lrs, map, node) for node in map if node[-1] == 'A']
    print(math.lcm(*periods))

if __name__ == "__main__":
    main()