from common import library
from functools import reduce

Coor = tuple[int, int, int]
Stone = tuple[Coor, Coor]

def intersection(s1: Stone, s2: Stone):
    p1, v1, p2, v2 = *s1, *s2

    det = v1[0] * v2[1] - v2[0] * v1[1]
    if det == 0:
        return

    t1 = (v2[1] * (p2[0] - p1[0]) - v2[0] * (p2[1] - p1[1])) / det
    t2 = (v1[1] * (p2[0] - p1[0]) - v1[0] * (p2[1] - p1[1])) / det

    if t1 >= 0 and t2 >= 0:
        intersection_x = p1[0] + t1 * v1[0]
        intersection_y = p1[1] + t1 * v1[1]
        return intersection_x, intersection_y


def parse_stone(s: str) -> int:
    l, r = s.split(' @ ')
    return tuple(map(int, l.split(','))), tuple(map(int, r.split(',')))

def main():
    stones = [parse_stone(s) for s in library.read_input(24)]
    mn, mx = 200000000000000, 400000000000000
    total = 0
    for i in range(len(stones)):
        for j in range(i + 1, len(stones)):
            if x := intersection(stones[i], stones[j]):
                total += mn <= x[0] <= mx and mn <= x[1] <= mx
    print(total)

if __name__ == "__main__":
    main()