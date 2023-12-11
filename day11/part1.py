from common import library
from functools import reduce

Grid = list[str]

def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

def transpose(grid: Grid) -> Grid:
    n, m = len(grid), len(grid[0])
    transposed_grid = [[None] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed_grid[j][i] = grid[i][j]
    return transposed_grid

def expand(grid: Grid) -> Grid:
    def expand_vertical(grid: Grid) -> Grid:
        expanded_grid = []
        for row in grid:
            if all(x == '.' for x in row):
                expanded_grid.extend([row, row])
            else:
                expanded_grid.append(row)
        return expanded_grid
    return compose(expand_vertical, transpose, expand_vertical, transpose)(grid)

def sum_of_galaxy_distances(grid: Grid) -> int: 
    n, m = len(grid), len(grid[0])
    galaxies = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '#']
    result = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            result += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    return result

def main():
    grid = list(map(list, library.read_input(11)))
    grid = expand(grid)
    print(sum_of_galaxy_distances(grid))

if __name__ == "__main__":
    main()