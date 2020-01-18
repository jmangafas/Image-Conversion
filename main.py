#libs

import os
import sys
from PIL import Image, ImageFilter

# accept arguments from the command line script execution.

folder_path = sys.argv

# setup the folder structure
existing_dir = os.chdir(r"C:\Users\jim\OneDrive - Dimension Data\Python\Code\images\venv" + str(folder_path[1]))
file_list = os.listdir(r"C:\Users\jim\OneDrive - Dimension Data\Python\Code\images\venv" + str(folder_path[1]))
new_dir = (r"C:\Users\jim\OneDrive - Dimension Data\Python\Code\images\venv" + str(folder_path[2]))
new_dir_check = os.listdir(r"C:\Users\jim\OneDrive - Dimension Data\Python\Code\images\venv")

# check if folder already exists in windows system.

try:
    if new_dir != new_dir_check:
        new_dir = os.mkdir(r"C:\Users\jim\OneDrive - Dimension Data\Python\Code\images\venv" + str(folder_path[2]))
except FileExistsError:
    print('\n'"Destination folder already exists")

new_dir = (r"C:\Users\jim\OneDrive - Dimension Data\Python\Code\images\venv" + str(folder_path[2]))
print('\n'"The following files will be converted to PNG. ")
print('\n', file_list)

# save each image file into new folder converting to a png.

for i in file_list:
    m = Image.open(i)
    m = m.save(new_dir + str('\\') + i[:-4] + ".png", format="png")

# inform the user of the location and rates

print('\n'"The processed files are now located in " + new_dir, "and named: ")
new_file_list = os.listdir(r"C:\Users\jim\OneDrive - Dimension Data\Python\Code\images\venv" + str(folder_path[2]))

print('\n', new_file_list)
