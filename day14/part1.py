from common import library
from functools import reduce

Grid = list[str]

def transpose(grid: Grid) -> Grid:
    n, m = len(grid), len(grid[0])
    transposed_grid = [[None] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed_grid[j][i] = grid[i][j]
    return transposed_grid

def count_horizontal_load(grid: Grid) -> int:
    total = 0
    for row in grid:
        curr_load = len(row)
        for i, x in enumerate(row, 1):
            if x == 'O':
                total += curr_load
                curr_load -= 1
            elif x == '#':
                curr_load = len(row) - i
    return total

def main():
    grid = library.read_input(14)
    print(count_horizontal_load(transpose(grid)))

if __name__ == "__main__":
    main()