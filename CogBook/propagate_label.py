import random

def propagate_label(node, neighbors, adjacency_matrix):
    # neighbors should be an iterable
    # returns nothing, just updates in place
    edge_weights = {}
    for neighbor in neighbors:
        edge_weights[neighbor.label] = adjacency_matrix[node.id][neighbor.id]
        for key in edge_weights:
            if neighbor.label == key:
                edge_weights[key] = edge_weights.get(neighbor.label) + adjacency_matrix[node.id][neighbor.id]
    node.label = max(edge_weights, key=edge_weights.get)