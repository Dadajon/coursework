# Created by dadajonjurakuziev at 2020/10/06 2:48 AM

import numpy as np

from sobel import sobel_edge_detection


def non_max_suppression(gradient_magnitude, gradient_direction):
    image_row, image_col = gradient_magnitude.shape

    output = np.zeros(gradient_magnitude.shape)

    PI = 180

    for row in range(1, image_row - 1):
        for col in range(1, image_col - 1):
            direction = gradient_direction[row, col]

            if (0 <= direction < PI / 8) or (15 * PI / 8 <= direction <= 2 * PI):
                before_pixel = gradient_magnitude[row, col - 1]
                after_pixel = gradient_magnitude[row, col + 1]

            elif (PI / 8 <= direction < 3 * PI / 8) or (9 * PI / 8 <= direction < 11 * PI / 8):
                before_pixel = gradient_magnitude[row + 1, col - 1]
                after_pixel = gradient_magnitude[row - 1, col + 1]

            elif (3 * PI / 8 <= direction < 5 * PI / 8) or (11 * PI / 8 <= direction < 13 * PI / 8):
                before_pixel = gradient_magnitude[row - 1, col]
                after_pixel = gradient_magnitude[row + 1, col]

            else:
                before_pixel = gradient_magnitude[row - 1, col - 1]
                after_pixel = gradient_magnitude[row + 1, col + 1]

            if gradient_magnitude[row, col] >= before_pixel and gradient_magnitude[row, col] >= after_pixel:
                output[row, col] = gradient_magnitude[row, col]

    return output


def threshold(image, low, high, weak):
    output = np.zeros(image.shape)

    strong = 255

    strong_row, strong_col = np.where(image >= high)
    weak_row, weak_col = np.where((image <= high) & (image >= low))

    output[strong_row, strong_col] = strong
    output[weak_row, weak_col] = weak

    return output


def hysteresis(image, weak):
    image_row, image_col = image.shape

    top_to_bottom = image.copy()

    for row in range(1, image_row):
        for col in range(1, image_col):
            if top_to_bottom[row, col] == weak:
                if top_to_bottom[row, col + 1] == 255 \
                        or top_to_bottom[row, col - 1] == 255 \
                        or top_to_bottom[row - 1, col] == 255 \
                        or top_to_bottom[row + 1, col] == 255 \
                        or top_to_bottom[row - 1, col - 1] == 255 \
                        or top_to_bottom[row + 1, col - 1] == 255 \
                        or top_to_bottom[row - 1, col + 1] == 255 \
                        or top_to_bottom[row + 1, col + 1] == 255:
                    top_to_bottom[row, col] = 255
                else:
                    top_to_bottom[row, col] = 0

    bottom_to_top = image.copy()

    for row in range(image_row - 1, 0, -1):
        for col in range(image_col - 1, 0, -1):
            if bottom_to_top[row, col] == weak:
                if bottom_to_top[row, col + 1] == 255 \
                        or bottom_to_top[row, col - 1] == 255 \
                        or bottom_to_top[row - 1, col] == 255 \
                        or bottom_to_top[row + 1, col] == 255 \
                        or bottom_to_top[row - 1, col - 1] == 255 \
                        or bottom_to_top[row + 1, col - 1] == 255 \
                        or bottom_to_top[row - 1, col + 1] == 255 \
                        or bottom_to_top[row + 1, col + 1] == 255:
                    bottom_to_top[row, col] = 255
                else:
                    bottom_to_top[row, col] = 0

    right_to_left = image.copy()

    for row in range(1, image_row):
        for col in range(image_col - 1, 0, -1):
            if right_to_left[row, col] == weak:
                if right_to_left[row, col + 1] == 255 \
                        or right_to_left[row, col - 1] == 255 \
                        or right_to_left[row - 1, col] == 255 \
                        or right_to_left[row + 1, col] == 255 \
                        or right_to_left[row - 1, col - 1] == 255 \
                        or right_to_left[row + 1, col - 1] == 255 \
                        or right_to_left[row - 1, col + 1] == 255 \
                        or right_to_left[row + 1, col + 1] == 255:
                    right_to_left[row, col] = 255
                else:
                    right_to_left[row, col] = 0

    left_to_right = image.copy()

    for row in range(image_row - 1, 0, -1):
        for col in range(1, image_col):
            if left_to_right[row, col] == weak:
                if left_to_right[row, col + 1] == 255 \
                        or left_to_right[row, col - 1] == 255 \
                        or left_to_right[row - 1, col] == 255 \
                        or left_to_right[row + 1, col] == 255 \
                        or left_to_right[row - 1, col - 1] == 255 \
                        or left_to_right[row + 1, col - 1] == 255 \
                        or left_to_right[row - 1, col + 1] == 255 \
                        or left_to_right[row + 1, col + 1] == 255:
                    left_to_right[row, col] = 255
                else:
                    left_to_right[row, col] = 0

    final_image = top_to_bottom + bottom_to_top + right_to_left + left_to_right

    final_image[final_image > 255] = 255

    return final_image


def canny_edge_detection(image):
    _, _, G, G_theta = sobel_edge_detection(image, convert_to_degree=True)
    nms_img = non_max_suppression(G, G_theta)
    threshold_img = threshold(nms_img, 50, 80, weak=400)
    canny_img = hysteresis(threshold_img, 400)

    return nms_img, threshold_img, canny_img
