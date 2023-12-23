from collections import defaultdict
from common import library

Graph = dict[tuple[int, int], set[tuple[int, int]]]

def build_graph(grid: list[str]) -> Graph:
    graph = defaultdict(set)
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch == '>':
                graph[(i, j)].add((i, j + 1))
                graph[(i, j - 1)].add((i, j))
            elif ch == 'v':
                graph[(i, j)].add((i + 1, j))
                graph[(i - 1, j)].add((i, j))
            elif ch == '.':
                for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '.':
                        graph[(ni, nj)].add((i, j))
                        graph[(i, j)].add((ni, nj))
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
        for e in graph[(i, j)]:
            q.append((*e, d + 1))
    return res


def main():
    grid = library.read_input(23)
    graph = build_graph(grid)
    print(dfs_max_path(graph, grid))

if __name__ == "__main__":
    main()