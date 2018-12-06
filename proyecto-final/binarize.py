import cv2
import os.path

folder_name = "./original_images/"
data_path = os.path.join(folder_name,'*g')
files = glob.glob(data_path)

for image_name in files:
    print(image_name)
