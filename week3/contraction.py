# coding=utf-8
import sys
import random


def get_min_cut(adjacency_matrix, edges):
    edges = edges.copy()
    nodes_count = len(adjacency_matrix)
    unions = {obj: {obj, } for obj in adjacency_matrix}

    # contract graph edges and merge respective endpoint nodes until 2 left
    while nodes_count > 2:
        # TODO: implement simple IndexedSet to avoid random.sample O(N)
        edge = random.sample(edges, 1)[0]
        edges.remove(edge)

        # assign node with smaller union to n1 (to reduce iterations count)
        n1, n2 = sorted(edge, key=lambda node: len(unions[node]))

        # remove self-loops created after merge of n1 and n2
        for node in unions[n1]:
            edges.difference_update(
                frozenset({node, adj_node})
                for adj_node in adjacency_matrix[node]
                if adj_node in unions[n2]
            )

        # merge 2 nodes unions (smaller into bigger)
        unions[n2] |= unions[n1]
        for node in unions[n1]:
            unions[node] = unions[n2]
        nodes_count -= 1
    return edges


def find_min_cut(adj_matrix):
    edges = {
        frozenset({edge, point})
        for edge, endpoints in adj_matrix.items()
        for point in endpoints
    }
    iterations = len(adj_matrix)
    return min(
        (get_min_cut(adj_matrix, edges) for _ in range(iterations)),
        key=len,
    )


if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = open(sys.argv[1])
        input_matrix = [map(int, line.split()) for line in f.readlines()]
        adjacency_matrix = {node: adj_list for node, *adj_list in input_matrix}
        min_cut = find_min_cut(adjacency_matrix)
        print("Edges: %d; Min cut size: %d" % (len(adjacency_matrix), len(min_cut)))
    else:
        print("Wrong arguments. Usage:\n 'python contraction.py graph.txt'")
