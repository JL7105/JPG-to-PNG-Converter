import os
import sys

from PIL import Image

# Grab first and second folder from command line.
original_folder, new_folder = sys.argv[1], sys.argv[2]
# If new folder doesn't exist, create a folder with that name.
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Loop through files in first folder.
# Open each file and save it in the new folder as png.
# Notify user of completion.
for file_name in os.listdir(original_folder):
    img = Image.open(f"{original_folder}{file_name}")
    clean_name = os.path.splitext(file_name)[0]
    img.save(f"{new_folder}{clean_name}.png", "png")
    print("All Done!")
