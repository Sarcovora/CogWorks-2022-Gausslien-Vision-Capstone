import numpy as np
import pickle

"""
profiles_dict is a dictionary that maps names to the corresponding Profile object
"""

class Profile:
    def __init__(self, name):
        self.name = name
        self.vectors = [] # Array of length 512 vectors
    def addVector(self, vector):
        self.vectors.append(vector)
    def clearVectors(self):
        self.vectors.clear()

def save_profiles_to_file(profiles_dict):
    with open('profiles.pkl','wb') as f:
        pickle.dump(f, profiles_dict)

def load_profiles_from_file():
    with open('profiles.pkl','rb') as f:
        return pickle.load(f)

def add_empty_profile(profiles_dict, name):
    profiles_dict[name] = Profile(name)
    
def remove_profile(profiles_dict, name):
    # assumes name is a valid key of profiles_dict
    conf = input("Confirm deletion of profile "+name+"? (y/n)")
    if conf=="y":
        del profiles_dict[name]

def save_vector_to_profile(profiles_dict, name, vector):
    if name not in profiles_dict:
        add_empty_profile(profiles_dict, name)
    profiles_dict[name].addVector(vector)
