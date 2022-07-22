import numpy as np
import random
from pathlib import Path

""" The full whiskers algorithm

Parameters:
    iterations (int): number of iterations
    nodes (list): list of all nodes
    adj_matrix (np.array): the adjacency matrix

Returns: None, but prints grouping history as a list and organizes the images based on their groupings
"""
def whiskers(iterations: int, nodes: list, adj_matrix: np.array):
    
    # the algorithm
    num_grouping_history = []
    for i in range(0, iterations):
        node = nodes[random.randint(0, len(nodes)-1)]
        propagate_label(node, node.neighbors, adj_matrix)
        groupings = connected_components(nodes)
        num_grouping_history.append(len(groupings))
    print(num_grouping_history)
    
    # moves the images into folders based on their groupings
    cwd = Path.cwd()
    for group_num in range(0, len(groupings)):
        
        # makes a folder to hold all the images in this group
        person_id = 'Person' + str(group_num+1)
        new_folder_path = cwd / person_id
        
        if Path.exists(new_folder_path):
            print("remove the folders from the previous run")
        else:
            new_folder_path.mkdir()
            
        # moves the images in this group
        for node in groupings[group_num]:
            file_path = node.file_path
            file_name = Path(file_path).name
            
            new_file_path = new_folder_path / file_name
            print(new_file_path)
            Path(file_path).rename(new_file_path)

"""
Tests to check if a single file can be moved properly
"""
def file_move_test(file_path: str, group_num: int):
    cwd = Path.cwd()
    person_id = 'Person' + str(group_num+1)
    new_folder_path = cwd / person_id
    
    print(new_folder_path)
    if Path.exists(new_folder_path):
            print("remove the folders from the previous run")
    else:
        new_folder_path.mkdir()
    
    file_name = Path(file_path).name
    print(file_name)
    
    new_file_path = new_folder_path / file_name
    print(new_file_path)
    Path(file_path).rename(new_file_path)
