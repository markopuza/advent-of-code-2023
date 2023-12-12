from common import library

Spring = tuple[str, list[int]]

CACHE = {}

def count_arrangements(row, groups):
    cache_key = (''.join(row), tuple(groups))
    if cache_key in CACHE:
        return CACHE[cache_key]
    
    if not row and groups:
        return 0
    # if not row and not groups:
    #     return 1
    if len(row) < sum(groups) + len(groups) - 1:
        return 0
    
    result = 0
    # try to do nothing
    if row[0] in '.?':
        result += count_arrangements(row[1:], groups)

    # try to place spring at the start of the row
    if all(x in '#?' for x in row[:groups[0]]):
        # this was the last group
        if len(groups) == 1:
            result += int(all(x in '.?' for x in row[groups[0]:]))
        elif row[groups[0]] != '#':
            result += count_arrangements(row[groups[0] + 1:], groups[1:])

    CACHE[cache_key] = result
    return result
    
def expand_spring(s: Spring) -> Spring:
    row, groups = s
    return list('?'.join([''.join(row)] * 5)), groups * 5

def parse_spring(spring_repr: str) -> Spring:
    s, gs = spring_repr.split()
    return list(s), list(map(int, gs.split(',')))

def main():
    springs = list(map(parse_spring, library.read_input(12)))
    springs = list(map(expand_spring, springs))
    print(sum(count_arrangements(*s) for s in springs))

if __name__ == "__main__":
    main()