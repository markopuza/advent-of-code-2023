from collections import defaultdict
from common import library

Grid = list[list[str]]
GearMask = list[list[set[int]]]

def get_gear_mask(grid: Grid) -> GearMask:
    nd, md = len(grid), len(grid[0])
    mask = [[set() for _ in range(md)] for _ in range(nd)]
    gear_number = 0
    for x in range(nd):
        for y in range(md):
            if grid[x][y] != '*':
                continue
            gear_number += 1
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < nd and 0 <= j <= md:
                        mask[i][j].add(gear_number)
    return mask

def get_gear_numbers(grid: Grid) -> list[int]:
    gears_to_numbers = defaultdict(list)
    mask = get_gear_mask(grid)
    nd, md = len(grid), len(grid[0])
    for x in range(nd):
        curr, gearset = '', set()
        for y in range(md):
            if grid[x][y] in '0123456789':
                curr += grid[x][y]
                gearset |= mask[x][y]
            else:
                if curr:
                    for g in gearset:
                        gears_to_numbers[g].append(int(curr))
                curr, gearset = '', set()
        if curr:
            for g in gearset:
                gears_to_numbers[g].append(int(curr))
    return [gears_to_numbers[g][0] * gears_to_numbers[g][1] for g in gears_to_numbers if len(gears_to_numbers[g]) == 2]


def main():
    grid = library.read_input(3)
    print(sum(get_gear_numbers(grid)))

if __name__ == "__main__":
    main()