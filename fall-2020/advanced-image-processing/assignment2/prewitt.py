# Created by dadajonjurakuziev at 2020/10/06 2:55 AM
import matplotlib.pyplot as plt
import numpy as np

from convolution import convolution


def prewitt_edge_detection(image):
    vertical_filter = np.array([[-1, 0, 1],
                                [-1, 0, 1],
                                [-1, 0, 1]])
    # array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    horizontal_filter = np.flip(vertical_filter.T, axis=0)

    prewitt_x = convolution(image, vertical_filter, verbose=False)
    prewitt_y = convolution(image, horizontal_filter, verbose=False)

    # calculate gradient magnitude
    prewitt = np.hypot(prewitt_x, prewitt_y)
    prewitt *= 255.0 / prewitt.max()

    return prewitt_x, prewitt_y, prewitt
