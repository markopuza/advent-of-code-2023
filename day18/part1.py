from common import library
from copy import deepcopy
from functools import reduce

Step = tuple[str, int, str]

def parse_step(s: str) -> Step:
    x, y, z = s.split()
    return (x, int(y), z[1:-1])

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    perimeter = 0.0
    # Apply the Shoelace formula
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
        perimeter += abs(x1 - x2) + abs(y1 - y2)

    return int(abs(area) / 2.0 + perimeter / 2.0)


def bulid_polygon(steps = list[Step]) -> list[str]:
    g = []
    currx, curry = 0, 0
    for dir, n, _ in steps:
        g.append((currx, curry))
        if dir == 'R':
            currx, curry = currx, curry + n
        if dir == 'L':
            currx, curry = currx, curry - n
        if dir == 'U':
            currx, curry = currx - n, curry
        if dir == 'D':
            currx, curry = currx + n, curry
    return g

def main():
    seq = [parse_step(s) for s in library.read_input(18)]
    polygon = bulid_polygon(seq)
    print(calculate_polygon_area(polygon))


if __name__ == "__main__":
    main()
