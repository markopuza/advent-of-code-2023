from bisect import bisect_left
from common import library

Grid = list[str]

def transpose(grid: Grid) -> Grid:
    n, m = len(grid), len(grid[0])
    transposed_grid = [[None] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transposed_grid[j][i] = grid[i][j]
    return transposed_grid

def sum_of_galaxy_distances(grid: Grid, expansion_rate: int = 1000000) -> int:
    def sum_vert_element(grid: Grid) -> int:
        result = 0
        empty_rows = [i for i, row in enumerate(grid) if all(x == '.' for x in row)]
        galaxies = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']
        for i in range(len(galaxies)):
            for j in range(i + 1, len(galaxies)):
                empty_rows_between = abs(bisect_left(empty_rows, galaxies[i][0]) - bisect_left(empty_rows, galaxies[j][0]))
                # print(galaxies[i], galaxies[j], empty_rows_between)
                result += abs(galaxies[i][0] - galaxies[j][0]) + (expansion_rate - 1) * empty_rows_between
        return result
    return sum_vert_element(grid) + sum_vert_element(transpose(grid))
    

def main():
    grid = list(map(list, library.read_input(11)))
    print(sum_of_galaxy_distances(grid))

if __name__ == "__main__":
    main()