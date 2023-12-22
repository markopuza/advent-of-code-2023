from common import library
from functools import reduce

Grid = list[str]

def find_possible_steps(grid: Grid, after: int = 0):
    n, m = len(grid), len(grid[0])
    sx, sy = next((x, y) for x in range(n) for y in range(m) if grid[x][y] == 'S')
    current = {(sx, sy)}
    is_valid = lambda x, y: 0 <= x < n and 0 <= y < m and grid[x][y] != '#'   
    for _ in range(after):
        current = reduce(set.union, [{(i, j) for i, j in [(cx-1,cy), (cx+1,cy), (cx, cy-1), (cx, cy+1)] if is_valid(i, j)} for cx, cy in current], set())
    return current

def main():
    grid = library.read_input(21)
    print(len(find_possible_steps(grid, 64)))

if __name__ == "__main__":
    main()