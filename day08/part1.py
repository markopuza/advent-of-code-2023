from common import library

Race = tuple[int]

def parse_instructions(instructions_desc: list[str]) -> tuple[str, dict[str, tuple[str]]]:
    lrs = instructions_desc[0]
    map = {}
    for row in instructions_desc[2:]:
        map[row.split(' =')[0]] = (row.split('(')[1].split(',')[0], row.split(', ')[1].split(')')[0])
    return lrs, map

def steps_between(lrs: str, map: dict[str, tuple[str]], source: str, destination: str):
    steps, curr = 0, source
    while curr != destination:
        curr = map[curr][0] if lrs[steps % len(lrs)] == 'L' else map[curr][1]
        steps += 1
    return steps

def main():
    lrs, map = parse_instructions(library.read_input(8))
    print(steps_between(lrs, map, 'AAA', 'ZZZ'))

if __name__ == "__main__":
    main()