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

for image_name in files:
    print(image_name)
    image = cv2.imread(image_name)
    small = cv2.resize(image, (0,0), fx=0.2, fy=0.2)
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    ret, threshold_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    binarized_image_name = image_name.replace(folder_name, destiny_folder_name)
    print(binarized_image_name)
    cv2.imwrite(binarized_image_name, threshold_image)
