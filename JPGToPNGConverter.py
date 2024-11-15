# Take command line parameters for folder containing images to be converted
# and a new folder name to be created for the converted images
# eg. JPGToPNGConverter.py Pokedex/ New/

import sys
import os
from PIL import Image

# 1. Get the arguments from the command line
def get_params():
    return sys.argv[1], sys.argv[2]


# 2. Check whether the new folder name exists and if not, create it
def create_new_folder(new_folder_name):
    try:
        os.chdir(new_folder_name)
    except FileNotFoundError as err:
        os.mkdir(new_folder_name)


# 3. Loop through the image folder and convert images to png
# 4. Save the new images to the new folder
def process_images(original_folder_name, new_folder_name):
    try:
        os.chdir(f"../{original_folder_name}")
        for file in os.listdir():
            with Image.open(file) as img:
                new_name = '../' + new_folder_name + '/' + file.split(".")[0] + '.png'
                img.save(new_name)
    except FileNotFoundError as err:
        print(err)
        print("Current directory: ", os.getcwd())
        print(original_folder_name)
        print(new_name)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Enter the arguments for the folders.")
    else:
        original_folder_name, new_folder_name = get_params()
        create_new_folder(new_folder_name)
        process_images(original_folder_name, new_folder_name)