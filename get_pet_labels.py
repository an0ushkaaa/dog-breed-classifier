import os

def get_pet_labels(image_dir):
    pet_labels = {}
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'):
            pet_name = " ".join(filename.lower().split('_')[:-1])
            pet_labels[filename] = [pet_name]
    return pet_labels
