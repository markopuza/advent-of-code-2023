from enum import Enum
from common import library
from functools import reduce

class Arrow(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

Grid = list[str]

def hash(s: str) -> int:
    return reduce(lambda v, ch: (ord(ch) + v)*17%256, s, 0)

def count_energised(grid: Grid) -> int:
    energised = set()
    beams = [(0, 0, Arrow.RIGHT)]
    while beams:
        x, y, arrow = beams[0]
        del beams[0]
        if (x, y, arrow) in energised or not (0 <= x < len(grid)) or not (0 <= y < len(grid[0])):
            continue
        energised.add((x, y, arrow))
        match arrow, grid[x][y]:
            case Arrow.UP, '.':
                beams.append((x - 1, y, Arrow.UP))
            case Arrow.DOWN, '.':
                beams.append((x + 1, y, Arrow.DOWN))
            case Arrow.LEFT, '.':
                beams.append((x, y - 1, Arrow.LEFT))
            case Arrow.RIGHT, '.':
                beams.append((x, y + 1, Arrow.RIGHT))

            case Arrow.UP, '/':
                beams.append((x, y + 1, Arrow.RIGHT))
            case Arrow.DOWN, '/':
                beams.append((x, y - 1, Arrow.LEFT))
            case Arrow.LEFT, '/':
                beams.append((x + 1, y, Arrow.DOWN))
            case Arrow.RIGHT, '/':
                beams.append((x - 1, y, Arrow.UP))

            case Arrow.UP, '\\':
                beams.append((x, y - 1, Arrow.LEFT))
            case Arrow.DOWN, '\\':
                beams.append((x, y + 1, Arrow.RIGHT))
            case Arrow.LEFT, '\\':
                beams.append((x - 1, y, Arrow.UP))
            case Arrow.RIGHT, '\\':
                beams.append((x + 1, y, Arrow.DOWN))

            case Arrow.UP, '-':
                beams.append((x, y - 1, Arrow.LEFT))
                beams.append((x, y + 1, Arrow.RIGHT))
            case Arrow.DOWN, '-':
                beams.append((x, y - 1, Arrow.LEFT))
                beams.append((x, y + 1, Arrow.RIGHT))
            case Arrow.LEFT, '-':
                beams.append((x, y - 1, Arrow.LEFT))
            case Arrow.RIGHT, '-':
                beams.append((x, y + 1, Arrow.RIGHT))

            case Arrow.UP, '|':
                beams.append((x - 1, y, Arrow.UP))
            case Arrow.DOWN, '|':
                beams.append((x + 1, y, Arrow.DOWN))
            case Arrow.LEFT, '|':
                beams.append((x - 1, y, Arrow.UP))
                beams.append((x + 1, y, Arrow.DOWN))
            case Arrow.RIGHT, '|':
                beams.append((x - 1, y, Arrow.UP))
                beams.append((x + 1, y, Arrow.DOWN))


    # visual = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    # for x, y, _ in energised:
    #     visual[x][y] = '#'
    # for r in visual:
    #     print(''.join(r))
    return len(set((x, y) for x, y, _ in energised))
            

def main():
    grid = library.read_input(16)
    print(count_energised(grid))

if __name__ == "__main__":
    main()