# Created by dadajonjurakuziev at 2020/10/06 2:33 AM
import matplotlib.pyplot as plt
import numpy as np


def convolution(image, kernel, average=False, verbose=False):
    if verbose:
        plt.title("Input image to convolution")
        plt.imshow(image, cmap='gray')
        plt.show()

    image_row, image_col = image.shape
    kernel_row, kernel_col = kernel.shape

    # zero padding
    output = np.zeros(image.shape)

    # calculate the size of the padding
    pad_height = int((kernel_row - 1) / 2)
    pad_width = int((kernel_col - 1) / 2)

    # create an empty numpy 2D array
    padded_image = np.zeros((image_row + (2 * pad_height), image_col + (2 * pad_width)))

    # copy the image to the proper location, apply padding
    padded_image[pad_height:padded_image.shape[0] - pad_height, pad_width:padded_image.shape[1] - pad_width] = image

    if verbose:
        plt.title("Zero padded image")
        plt.imshow(padded_image, cmap='gray')
        plt.show()

    # convolution operation
    for row in range(image_row):
        for col in range(image_col):
            output[row, col] = np.sum(
                kernel * padded_image[row:row + kernel_row, col:col + kernel_col])

            # apply the smooth/blur effect
            if average:
                output[row, col] /= kernel.shape[0] * kernel.shape[1]

    if verbose:
        plt.title("Conv output image using {}X{} filter".format(kernel_row, kernel_col))
        plt.imshow(output, cmap='gray')
        plt.show()

    return output
