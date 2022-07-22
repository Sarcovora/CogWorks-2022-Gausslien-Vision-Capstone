#haven't tested yet
import skimage.io as io
import numpy as np
from get_descriptors import get_descriptors
from cos_distance import cos_distance
from facenet_models import FacenetModel


def nodes_adj_graph(image_paths:list):
    """
    Parameters
    ----------
       image_matrix: List, shape = (N,)
           List of image-paths
       
    Returns
    ----------
       nodes: List[Node], shape = (N,)
           List of nodes for each image
       adj_graph: np.array, shape = (N,N)
           A numpy array storing the weighted adjacency matrix of all nodes
       
    """
    threshold = 0.5 #need to change later
    N = len(image_paths) #N = number of nodes
    model = FacenetModel()
    descriptors = np.ndarray(N, dtype = np.ndarray)
    nodes = []
    adj_graph = np.zeros((N, N))
    
    for i in range(N):
        image = io.imread(image_paths[i])
        if image.shape[-1] == 4:
            image = image[..., :-1]
            descriptors[i] = get_descriptors(image)
        
    
    for i in range(N): 
        for j in range(N):
            if (i == j):
                continue
            distance = cos_distance(descriptors[i], descriptors[j])
            if (distance < threshold):
                adj_graph[i,j] = 1/(distance**2)
                adj_graph[j,i] = 1/(distance**2)
        nodes.append(Node(i, np.nonzeros(adj_matrix[i]), descriptors[i]))
            
    return nodes, adj_graph
    
    
