from __future__ import division
import cv2
import os.path
import glob

folder_name = "./original_images/"
destiny_folder_name = "./binary_images/"
data_path = os.path.join(folder_name,'*G')
G_files = glob.glob(data_path)
data_path = os.path.join(folder_name,'*g')
g_files = glob.glob(data_path)
files = g_files + G_files

# Parameters for image size:

width_objective = 100

for image_name in files:
    # Read
    image = cv2.imread(image_name)
    # Resize
    ratio = width_objective / image.shape[1]
    dim = (width_objective, int(image.shape[0] * ratio))
    height, width = image.shape[:2]
    small = image
    if width_objective < width:
        small = cv2.resize(small, dim)
    # To grayscale
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    # Binarize
    ret, threshold_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    binarized_image_name = image_name.replace(folder_name, destiny_folder_name)
    cv2.imwrite(binarized_image_name, threshold_image)
