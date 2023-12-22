from common import library
Grid = list[str]

def find_possible_steps(grid: Grid, after: int = 0):
    n, m = len(grid), len(grid[0])
    G = {(x, y) for x in range(n) for y in range(m) if grid[x][y] != '#'}
    sx, sy = next((x, y) for x in range(n) for y in range(m) if grid[x][y] == 'S')
    current = {(sx, sy)}
    is_valid = lambda x, y: (x % n, y % m) in G
    for i in range(after):
        # print(f'{i}/{after}')
        current = {(i, j) for cx, cy in current for i, j in [(cx-1,cy), (cx+1,cy), (cx, cy-1), (cx, cy+1)] if is_valid(i, j)}
    return len(current)

def main():
    grid = library.read_input(21)
    v1 = (0,  find_possible_steps(grid, 65))
    print(v1)
    v2 = (1,  find_possible_steps(grid, 65 + 1 * 131))
    print(v2)
    v3 = (2,  find_possible_steps(grid, 65 + 2 * 131))
    print(v3)

    a, b, c = v1[1], v2[1], v3[1]
    n = 26501365 // 131
    print( a+n*(b-a+(n-1)*(c-b-b+a)//2) )

if __name__ == "__main__":
    main()