import shutil
import sys
from PIL import Image
import os

# Grab first and second argument
initialFolder = sys.argv[1]
newFolder = sys.argv[2]


# Check if new exists, if not create
def is_Directory(folder):
    if os.path.isdir(folder):
        return False
    else:
        os.makedirs(folder)


is_Directory(sys.argv[2])


# loop through Pokedex
def loop_through_Folder(folder):
    for file in os.scandir(folder):
        if file.is_file():
            yield os.path.basename(file)


# Convert Images to png
def convert_Image_to_png(file, newFolder):
    newfile, e = os.path.splitext(file)
    newfile = newfile + ".png"
    imgfile = Image.open(sys.argv[1] + "\\" + file)
    imgfile = imgfile.copy()
    newfile = imgfile.save(sys.argv[2] + "\\" + newfile)

#Loop through folder and convert it to a png
for l in loop_through_Folder(sys.argv[1]):
    convert_Image_to_png(l, newFolder)
