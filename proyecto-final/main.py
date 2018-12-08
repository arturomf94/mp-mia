from __future__ import division
from noise import sp_noise
from graph import create_graph, add_costs, recover_image
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random
import cv2
import os.path
import glob

# Sort paths for binarization
folder_name = "./original_images/"
binary_folder_name = "./binary_images/"
noise_folder_name = "./noisy_images/"
clean_folder_name = "./clean_images/"
data_path = os.path.join(folder_name,'*G')
G_files = glob.glob(data_path)
data_path = os.path.join(folder_name,'*g')
g_files = glob.glob(data_path)
files = g_files + G_files

# Parameters for image size and noise:
width_objective = 100
noise_percentage = .01
pairwise_cost = 1
unary_matching_cost_source = .9
unary_matching_cost_sink = .9
unary_nonmatching_cost_source = 1
unary_nonmatching_cost_sink = 1

# Loop over all images to resize and binarize:
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
    # Convert to grayscale
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    # Convert to binary
    ret, binary_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # Save binary image
    binarized_image_name = image_name.replace(folder_name, binary_folder_name)
    cv2.imwrite(binarized_image_name, binary_image)
    # Add noise:
    noisy_image = sp_noise(binary_image, noise_percentage)
    # Save noisy image
    noisy_image_name = image_name.replace(folder_name, noise_folder_name)
    cv2.imwrite(noisy_image_name, noisy_image)
    G = create_graph(noisy_image)
    add_costs(G, unary_matching_cost_source,
                unary_nonmatching_cost_source,
                unary_matching_cost_sink,
                unary_nonmatching_cost_sink,
                pairwise_cost)
    # Max Flow
    flow_value, flow_dict = nx.maximum_flow(G, 1, 0)
    cut_value, partition = nx.minimum_cut(G,1, 0)
    # Denoise image
    clean_image = recover_image(noisy_image, partition)
    clean_image_name = image_name.replace(folder_name, clean_folder_name)
    cv2.imwrite(clean_image_name, clean_image)
