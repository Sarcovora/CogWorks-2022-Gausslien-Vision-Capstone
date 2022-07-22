from CogBook import label_faces
from PIL import Image
from camera import take_picture
import numpy as np

while True:
    choice = input("Upload (u) or take a photo (c)? ")
    
    if choice=="u":
        filepath = input("Filepath: ")
        pic = np.array(Image.open(filepath))[:,:,:3]
        label_faces(pic)
        break
    elif choice=="c":
        pic = take_picture()
        label_faces(pic)
        break
    else:
        print("Invalid input. Try again. ")
