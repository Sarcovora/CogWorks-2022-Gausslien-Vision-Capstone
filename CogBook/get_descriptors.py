from facenet_models import FacenetModel

def get_descriptors(image_data):
    """
    Returns a descriptors numpy array.

    Parameters
    ----------
    image_data : numpy.ndarray, shape-(R, C, 3) (RGB is the last dimension)
        Pixel information for the image.
    
    Returns
    -------
    np.ndarray, shape-(N, 512)
        The descriptor vectors, where N is the number of faces.
    """
    
    model = FacenetModel()
    boxes, probabilities, _ = model.detect(image_data)
    descriptors = model.compute_descriptors(image_data, boxes)
    for prob in probabilities:
        print(prob)
    return descriptors
