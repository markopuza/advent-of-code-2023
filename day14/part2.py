from common import library
from functools import reduce
from copy import deepcopy

Grid = list[str]

def rotate_cw(grid: Grid) -> Grid:
    n, m = len(grid), len(grid[0])
    rotated = [[None] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated[j][n - 1 - i] = grid[i][j]
    return rotated

def count_horizontal_load(grid: Grid) -> int:
    return sum(len(grid) - j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 'O')

def cycle(grid: Grid) -> int:
    for _ in range(4):
        updated_grid = [['.'] * len(grid[0]) for _ in range(len(grid))]
        for i, row in enumerate(grid):
            curr = 0
            for j, x in enumerate(row):
                if x == 'O':
                    updated_grid[i][curr] = 'O'
                    curr += 1
                elif x == '#':
                    updated_grid[i][j] = '#'
                    curr = j + 1
        grid = rotate_cw(updated_grid)
    return grid
    
PERIOD_CACHE = {}
def find_period(grid: Grid) -> tuple[int, int]:
    def key(grid: Grid) -> str:
        return ''.join(''.join(r) for r in grid)
    i = 0
    while True:
        i += 1
        grid = cycle(grid)
        k = key(grid)
        if k in PERIOD_CACHE:
            return PERIOD_CACHE[k], i - PERIOD_CACHE[k]
        PERIOD_CACHE[k] = i

def main():
    orig_grid = rotate_cw(rotate_cw(rotate_cw(library.read_input(14))))
    grid = deepcopy(orig_grid)
    start, period = find_period(grid)
   
    print(f'start: {start}, period: {period}')

    grid = deepcopy(orig_grid)
    for cnt in range(start + (1000000000 - start) % period):
        grid = cycle(grid)
        print(cnt, count_horizontal_load(grid))
    
    print(count_horizontal_load(grid))

        

if __name__ == "__main__":
    main()