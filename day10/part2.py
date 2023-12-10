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

def get_inside_area(maze: Maze, distance_mask: list[list[int]]) -> int:
    area = 0
    for row, mrow in zip(maze, distance_mask):
        intersection_number = 0
        last_corner = None
        for x, d in zip(row, mrow):
            if d >= 0:
                if x == '|':
                    intersection_number += 1
                    last_corner = None
                elif x == '7' and last_corner == 'L':
                    intersection_number += 1
                    last_corner = None
                elif x == 'J' and last_corner == 'F':
                    intersection_number += 1
                    last_corner = None
                elif x == 'L':
                    last_corner = 'L'
                elif x == 'F':
                    last_corner = 'F'
                elif x not in '-S':
                    last_corner = None
            else:
                last_corner = None
            if d == -1: # not in the main loop
                area += intersection_number & 1
        # print(row, area)
    return area


def main():
    maze = library.read_input(10)
    distance_mask = get_distance_mask(maze)
    print(get_inside_area(maze, distance_mask))


if __name__ == "__main__":
    main()