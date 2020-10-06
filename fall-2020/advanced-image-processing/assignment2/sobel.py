# Created by dadajonjurakuziev at 2020/10/06 2:46 AM
import argparse

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

from convolution import convolution
from gaussian import gaussian_blur


def sobel_edge_detection(image, filter):
    image_x = convolution(image, filter)

    # generate intermediate images
    plt.imshow(image_x, cmap='gray')
    plt.title("Horizontal Edge")
    plt.show()

    image_y = convolution(image, filter.T)


    plt.imshow(image_y, cmap='gray')
    plt.title("Vertical Edge")
    plt.show()
    
    # calculate gradiednt magnitude
    # np.hypot() = sqrt(img_x**2 + img_2**2) -> hypotenuse
    G = np.hypot(image_x, image_y)

    G *= 255.0 / G.max()


    plt.imshow(G, cmap='gray')
    plt.title("Gradient Magnitude")
    plt.show()
        
    # calculate gradient angle
    G_theta = np.arctan2(image_y, image_x)

    if convert_to_degree:
        G_theta = np.rad2deg(gradient_direction)
        G_theta += 180

    return G, G_theta

