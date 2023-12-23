from collections import defaultdict
from common import library
from copy import deepcopy

Graph = dict[tuple[int, int], set[tuple[int, int]]]

def build_graph(grid: list[str]) -> Graph:
    graph = defaultdict(set)
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch != '#':
                for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '.':
                        graph[(ni, nj)].add((i, j, 1))
                        graph[(i, j)].add((ni, nj, 1))
        
    while 1:
        for (i, j), edges in graph.items():
            if len(edges) == 2:
                (i1, j1, d1), (i2, j2, d2) = edges
                graph[(i1, j1)].remove((i, j, d1))
                graph[(i2, j2)].remove((i, j, d2))
                graph[(i1, j1)].add((i2, j2, d1 + d2))
                graph[(i2, j2)].add((i1, j1, d1 + d2))
                del graph[(i, j)]
                break
        else:
            break
    return graph

def dfs_max_path(graph: Graph, grid: list[str]) -> int:
    n, m = len(grid), len(grid[0])
    q, visited, res = [(0, 1, 0)], set(), 0
    while q:
        i, j, d = q.pop()
        if d == -1:
            visited.remove((i, j))
            continue
        if i == n - 1 and j == m - 2:
            res = max(res, d)
            continue
        if (i, j) in visited:
            continue
        visited.add((i, j))
        q.append((i, j, -1))
        for ni, nj, nd in graph[(i, j)]:
            q.append((ni, nj, d + nd))
    return res


def main():
    grid = library.read_input(23)
    graph = build_graph(grid)
    print(dfs_max_path(graph, grid))

if __name__ == "__main__":
    main()