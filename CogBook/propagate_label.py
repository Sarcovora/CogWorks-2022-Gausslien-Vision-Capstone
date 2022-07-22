import random

def propagate_label(node, neighbors, adjacency_matrix):
    # neighbors should be an iterable
    # returns nothing, just updates in place
    highest_weight = 0
    for neighbor in neighbors:
        if adjacency_matrix[node.id][neighbor.id] > highest_weight:
            highest_weight = adjacency_matrix[node.id][neighbor.id]
            node.label = neighbor.label
        elif adjacency_matrix[node.id][neighbor.id] == highest_weight:
            if random.random() > 0.5:
                node.label = neighbor.label