from common import library
from functools import reduce

Grid = list[list[str]]
Mask = list[list[bool]]

def get_mask(grid: Grid) -> Mask:
    symbols = reduce(set.union, (set(l) for l in grid), set()) - set('.0123456789')
    nd, md = len(grid), len(grid[0])
    mask = [[False] * md for _ in range(nd)]
    for x in range(nd):
        for y in range(md):
            if grid[x][y] not in symbols:
                continue
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < nd and 0 <= j <= md:
                        mask[i][j] = True
    return mask

def get_part_numbers(grid: Grid) -> list[int]:
    part_numbers = []
    mask = get_mask(grid)
    nd, md = len(grid), len(grid[0])
    for x in range(nd):
        curr, curr_is_part = '', False
        for y in range(md):
            if grid[x][y] in '0123456789':
                curr += grid[x][y]
                curr_is_part |= mask[x][y]
            else:
                if curr and curr_is_part:
                    part_numbers.append(int(curr))
                curr, curr_is_part = '', False
        if curr and curr_is_part:
            part_numbers.append(int(curr))
    return part_numbers


def main():
    grid = library.read_input(3)
    print(sum(get_part_numbers(grid)))

if __name__ == "__main__":
    main()