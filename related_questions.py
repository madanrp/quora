__author__ = 'madanp'
from collections import defaultdict
if __name__ == "__main__":
    num_nodes = int(raw_input())
    weights = map(int, raw_input().split())
    adjacency_matrix = defaultdict(set)
    for i in range(num_nodes-1):
        u, v = map(int, raw_input().split())
        adjacency_matrix[u].add(v)
        adjacency_matrix[v].add(u)

    print adjacency_matrix