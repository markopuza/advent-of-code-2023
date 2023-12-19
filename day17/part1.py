from common import library
import heapq

def minimal_heat(start, end, graph):
    queue = [(0, 0, 0, 0, 0)]
    seen = set()
    while queue:
        heat, x, y, px, py = heapq.heappop(queue)
        if (x, y) == end:
            return heat
        if (x, y, px, py) in seen:
            continue
        seen.add((x, y, px, py))

        # We have to turn
        for dx, dy in {(1,0), (0,1), (-1,0), (0,-1)} - {(px, py), (-px, -py)}:
            currx, curry, h = x, y, heat
            for i in range(1, 4):
                currx += dx
                curry += dy
                if (currx, curry) in graph:
                    h += graph[currx, curry]
                    heapq.heappush(queue, (h, currx, curry, dx, dy))

def parse_grid(grid):
    return {(i, j): int(grid[i][j]) for i in range(len(grid)) for j in range(len(grid[0]))}

def main():
    grid = library.read_input(17)
    graph = parse_grid(grid)
    print(minimal_heat((0, 0), max(graph), graph))

if __name__ == "__main__":
    main()