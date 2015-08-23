__author__ = 'madanp'
from collections import defaultdict
from operator import itemgetter
import random

def farthest_node(node, node_weight, adjacency_matrix, retain_path=False):
    visited = set([node])
    stack = [(node, node_weight, [])]
    while stack:
        node, weight, path = stack.pop(0)
        for neighbor, n_weight in sorted(adjacency_matrix[node], key=itemgetter(1)):
            if neighbor not in visited:
                visited.add(neighbor)
                if retain_path:
                    stack.append((neighbor, n_weight + weight, path + [node]))
                else:
                    stack.append((neighbor, n_weight + weight, path))
        if not stack:
            return node, (path + [node])

if __name__ == "__main__":
    num_nodes = int(raw_input())
    weights = map(int, raw_input().split())
    adjacency_matrix = defaultdict(set)
    for i in range(num_nodes-1):
        u, v = map(int, raw_input().split())
        adjacency_matrix[u].add((v, weights[v-1]))
        adjacency_matrix[v].add((u, weights[u-1]))

    if num_nodes == 1:
        print 1
    #elif num_nodes == 2:
    #    print 1
    else:
        random_node = random.randint(1, num_nodes)
        node, path = farthest_node(random_node, weights[random_node-1], adjacency_matrix)
        node, path = farthest_node(node, weights[node-1], adjacency_matrix, True)
        print path
        print path[len(path)/2]
