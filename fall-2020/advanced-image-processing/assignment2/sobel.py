# Created by dadajonjurakuziev at 2020/10/06 2:46 AM

import matplotlib.pyplot as plt
import numpy as np

from convolution import convolution


def sobel_edge_detection(image, convert_to_degree=False, verbose=False):
    vertical_filter = np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])
    # array([[-1, -2, -1],[ 0,  0,  0],[ 1,  2,  1]])
    horizontal_filter = vertical_filter.T

    image_x = convolution(image, vertical_filter, verbose=False)
    image_y = convolution(image, horizontal_filter, verbose=False)

    # generate intermediate images
    if verbose:
        plt.title("Sobel horizontal edge")
        plt.imshow(image_x, cmap='gray')
        plt.show()

        plt.title("Sobel vertical edge")
        plt.imshow(image_y, cmap='gray')
        plt.show()

    # calculate gradient magnitude
    # np.hypot() = sqrt(img_x**2 + img_2**2) -> hypotenuse
    G = np.hypot(image_x, image_y)

    G *= 255.0 / G.max()

    if verbose:
        plt.title("Sobel gradient magnitude")
        plt.imshow(G, cmap='gray')
        plt.show()

    # calculate gradient direction
    G_theta = np.arctan2(image_y, image_x)

    if convert_to_degree:
        G_theta = np.rad2deg(G_theta)
        G_theta += 180

    return image_x, image_y, G, G_theta
