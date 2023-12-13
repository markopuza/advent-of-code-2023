from common import library
from functools import reduce
from copy import deepcopy

Grid = list[str]

def parse_grids(grids_input: list[str]) -> list[Grid]:
    return [g.split('\n') for g in ('\n'.join(grids_input)).split('\n\n')]

def transpose(grid: Grid) -> Grid:
    n, m = len(grid), len(grid[0])
    transposed_grid = [[None] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed_grid[j][i] = grid[i][j]
    return transposed_grid

def get_vertical_reflection_points(row: str) -> list[int]:
    reflection_points = []
    lrow = list(row)
    for i in range(1, len(row)):
        left = ''.join(lrow[:i][::-1])
        right = ''.join(lrow[i:])
        l = min(len(left), len(right))
        if left[:l] == right[:l]:
            reflection_points.append(i)
    return reflection_points

def get_vertical_reflection_lines(grid: Grid) -> list[int]:
    return list(reduce(set.__and__, [set(get_vertical_reflection_points(r)) for r in grid]))

def repair_smudge(grid: Grid) -> tuple[set[int], set[int]]:
    orig_vert = set(get_vertical_reflection_lines(grid))
    orig_hor = set(get_vertical_reflection_lines(transpose(grid)))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cp = deepcopy(list(map(list, grid)))
            cp[i][j] = '.' if cp[i][j] == '#' else '#'
            vert = set(get_vertical_reflection_lines(cp))
            hor = set(get_vertical_reflection_lines(transpose(cp)))
            if (vert - orig_vert) or (hor - orig_hor):
                return vert - orig_vert, hor - orig_hor


def get_sum(grids: list[Grid]) -> int:
    total = 0
    for g in grids:
        new_vert, new_hor = repair_smudge(g)
        total += sum(new_vert)
        total += 100*sum(new_hor)
    return total

def main():
    grids = parse_grids(library.read_input(13))
    print(get_sum(grids))

if __name__ == "__main__":
    main()