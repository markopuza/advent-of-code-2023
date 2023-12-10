from common import library

Maze = list[str]

VALID_UP = {
    '|': '|7F',
    '-': '',
    'L': '|7F',
    'J': '|7F',
    '7': '',
    'F': '',
    'S': '|7F',
}
VALID_DOWN = {
    '|': '|JL',
    '-': '',
    'L': '',
    'J': '',
    '7': '|JL',
    'F': '|JL',
    'S': '|JL',
}
VALID_LEFT = {
    '|': '',
    '-': '-FL',
    'L': '',
    'J': '-FL',
    '7': '-FL',
    'F': '',
    'S': '-FL',
}
VALID_RIGHT = {
    '|': '',
    '-': '-J7',
    'L': '-J7',
    'J': '',
    '7': '',
    'F': '-J7',
    'S': '-J7',
}

def get_distance_mask(maze: Maze) -> list[list[int]]:
    n, m = len(maze), len(maze[0])
    mask = [[-1] * m for _ in range(n)]
    sx, sy = [[x, y] for x in range(n) for y in range(m) if maze[x][y] == 'S'][0]
    curr, d = [(sx, sy)], 0
    while curr:
        # print(curr)
        next_curr = []
        for x, y in curr:
            if mask[x][y] != -1:
                continue
            mask[x][y] = d
            if x > 0 and maze[x-1][y] in VALID_UP[maze[x][y]]:
                next_curr.append((x - 1, y))
            if x < n - 1 and maze[x + 1][y] in VALID_DOWN[maze[x][y]]:
                next_curr.append((x + 1, y))
            if y > 0 and maze[x][y-1] in VALID_LEFT[maze[x][y]]:
                next_curr.append((x, y - 1))
            if y < m - 1 and maze[x][y+1] in VALID_RIGHT[maze[x][y]]:
                next_curr.append((x, y + 1))
        curr = next_curr
        d += 1
    return mask

def main():
    maze = library.read_input(10)
    distance_mask = get_distance_mask(maze)
    # for r in distance_mask: print(r)
    print(max(max(r) for r in distance_mask))


if __name__ == "__main__":
    main()