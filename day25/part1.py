from collections import defaultdict
from common import library
import random
from copy import deepcopy

Graph = dict[str, set[str]]


def contract(graph, u, v, SIZES):
    # Contract edge (u, v) by merging node v into node u
    graph[u] += graph[v]
    SIZES[u] += SIZES[v]
    del graph[v]
    del SIZES[v]
    for node, neighbors in graph.items():
        graph[node] = [u if n == v else n for n in neighbors if n != node]
        graph[node] = list(filter(lambda x: x != node, graph[node]))
    return graph

def karger_min_cut(graph):
    SIZES = {k: 1 for k in graph}
    while len(graph) > 2:
        # Randomly choose an edge (u, v)
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        # Contract the edge
        graph = contract(graph, u, v, SIZES)

    # The remaining edges represent a cut
    min_cut_size = len(graph[list(graph.keys())[0]])

    return min_cut_size, SIZES


def build_graph(rows: list[str]) -> Graph:
    g = defaultdict(list)
    for r in rows:
        s, ts = r.split(': ')
        for t in ts.split():
            g[s].append(t)
            g[t].append(s)
    return g

def main():
    rows = library.read_input(25)
    g = build_graph(rows)

    min_cut, min_sizes = float('inf'), None
    tries = 1000
    for i in range(tries):
        print(f'{i}/{tries}')
        mc, sizes = karger_min_cut(deepcopy(g))
        if mc < min_cut:
            min_cut, min_sizes = mc, tuple(sizes.values())
        print(min_cut, min_sizes)


if __name__ == "__main__":
    main()