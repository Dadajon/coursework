# Created by dadajonjurakuziev at 2020/10/06 7:25 PM
import numpy as np
from PIL import Image

from canny import canny_edge_detection
from gaussian import gaussian_blur
from prewitt import prewitt_edge_detection
from sobel import sobel_edge_detection
from utils import save_output
import argparse

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    input_img_path = args["image"]
    folder_name = input_img_path.split('/')[1].split('.')[0]

    # open image as numpy array
    image = np.array(Image.open(input_img_path).convert(mode='L'))
    # gaussian blur
    blur_image = gaussian_blur(image, kernel_size=3, verbose=False)

    # sobel
    sobel_x, sobel_y, sobel, _ = sobel_edge_detection(blur_image, convert_to_degree=False)

    # prewitt
    prewitt_x, prewitt_y, prewitt = prewitt_edge_detection(blur_image)

    # canny
    # 1D Gaussian mask
    image_1D = gaussian_blur(image, kernel_size=1, verbose=False)
    nms, threshold, canny = canny_edge_detection(image_1D)

    # save results
    save_output(folder_name, sobel_x, sobel_y, sobel, prewitt_x, prewitt_y, prewitt, nms, threshold, canny)
