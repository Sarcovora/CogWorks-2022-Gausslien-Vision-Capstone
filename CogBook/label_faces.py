import numpy as np
from facenet_models import FacenetModel
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.pyplot import text

from PIL import Image

from profile_functionality import query_database

def label_faces(image_data):
    """
    Displays an image with boxes around people's faces and labels them with names.

    Parameters
    ----------
    image_data : numpy.ndarray, shape-(R, C, 3) (RGB is the last dimension)
        Pixel information for the image.
    """
    
    # this will download the pretrained weights (if they haven't already been fetched)
    # which should take just a few seconds
    model = FacenetModel()

    # detect all faces in an image
    # returns a tuple of (boxes, probabilities, landmarks)
    boxes, probabilities, _ = model.detect(image_data)

    # producing a face descriptor for each face
    # returns a (N, 512) array, where N is the number of boxes
    # and each descriptor vector is 512-dimensional
    descriptors = model.compute_descriptors(image_data, boxes)

    names = []
    for d in descriptors:
        names.append(query_database(d))
    
    fig, ax = plt.subplots()
    ax.imshow(image_data)

    i = 0
    for box, prob in zip(boxes, probabilities):
        # draw the box on the screen
        ax.add_patch(Rectangle(box[:2], *(box[2:] - box[:2]), fill=None, lw=2, color="red"))
        # add names to the box
        ax.text(*box[:2],
                names[i],
                size=12,
                va="center",
                bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8),))
        i += 1