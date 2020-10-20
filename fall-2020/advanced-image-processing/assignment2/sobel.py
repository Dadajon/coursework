# Created by dadajonjurakuziev at 2020/10/06 2:46 AM
import numpy as np

from convolution import convolution


def sobel_edge_detection(image, convert_to_degree=False):
    vertical_filter = np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]])
    horizontal_filter = vertical_filter.T  # array([[-1, -2, -1],[ 0,  0,  0],[ 1,  2,  1]])

    sobel_x = convolution(image, vertical_filter, verbose=False)
    sobel_y = convolution(image, horizontal_filter, verbose=False)

    # calculate gradient magnitude
    G = np.hypot(sobel_x, sobel_y)  # np.hypot() = sqrt(img_x**2 + img_2**2) -> hypotenuse
    G *= 255.0 / G.max()

    # calculate gradient direction
    G_theta = np.arctan2(sobel_x, sobel_y)

    if convert_to_degree:
        G_theta = np.rad2deg(G_theta)
        G_theta += 180

    return sobel_x, sobel_y, G, G_theta
