from CogBook import *
from PIL import Image
from shutil import move

import pickle
import numpy as np
import os



# assign directory
directory = '../Images'
loadedDir = '../Loaded_Images'

# iterate over files in
# that directory
fileList = []

for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    destination = os.path.join(loadedDir, filename)
    
    if os.path.isfile(filepath):
        fileList.append((filepath, filename, destination))


profileDB = load_profiles_from_file()

for fileInfo in fileList:
    print(fileInfo[1])

    name, number = fileInfo[1].split(".")[0].split("_")
    
    img_data = np.array(Image.open(fileInfo[0]))[:,:,:3]
    descriptors = get_descriptors(img_data)
    
    save_vector_to_profile(profileDB, name, descriptors)
    
    move(fileInfo[0], fileInfo[2])
    
save_profiles_to_file(profileDB)