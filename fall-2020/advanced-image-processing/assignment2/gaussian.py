# Created by dadajonjurakuziev at 2020/10/06 2:33 AM
import matplotlib.pyplot as plt
import numpy as np

from convolution import convolution


# calculate the density using the formula of normal distribution.
def dnorm(x, mu, sd):
    return 1 / (np.sqrt(2 * np.pi) * sd) * np.e ** (-np.power((x - mu) / sd, 2) / 2)


# generate Gaussian Kernel
def gaussian_kernel(size, sigma=1.4, verbose=False):
    kernel_1D = np.linspace(-(size // 2), size // 2, size)
    for i in range(size):
        kernel_1D[i] = dnorm(kernel_1D[i], 0, sigma)
    kernel_2D = np.outer(kernel_1D.T, kernel_1D.T)

    kernel_2D *= 1.0 / kernel_2D.max()

    if verbose:
        plt.title("Gaussian kernel ( {}X{} )".format(size, size))
        plt.imshow(kernel_2D, cmap='gray')
        plt.show()

    return kernel_2D


def gaussian_blur(image, kernel_size, sigma=1.4, verbose=False):
    kernel = gaussian_kernel(kernel_size, sigma=sigma, verbose=verbose)
    return convolution(image, kernel, average=True, verbose=verbose)
