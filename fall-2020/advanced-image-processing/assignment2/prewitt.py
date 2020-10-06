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

    image_x = convolution(image, vertical_filter, verbose=False)
    image_y = convolution(image, horizontal_filter, verbose=False)

    # generate intermediate images
    plt.title("Prewitt horizontal edge")
    plt.imshow(image_x, cmap='gray')
    plt.show()

    plt.title("Prewitt vertical edge")
    plt.imshow(image_y, cmap='gray')
    plt.show()

    plt.title("Prewitt edge")
    plt.imshow(image_x + image_y, cmap='gray')
    plt.show()

    return image_x, image_y, image_x+image_y
