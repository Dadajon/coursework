# Created by dadajonjurakuziev at 2020/09/29 2:44 PM

import numpy as np
from PIL import Image


# TODO: Read the image and let it be named with O.
def read_img(img):
    O = Image.open(img)
    O.save("images/output/O.jpg")
    return O


# TODO: Take pixel values in the rectangular area designated by two corner points (300, 300) and (340,340) from the image O.
#       Let the image be named with S. Print the pixel values of S. Also, display the image S on the monitor.
def crop_img(img):
    x1, y1, x2, y2 = 300, 300, 340, 340
    area = (x1, y1, x2, y2)
    S = img.crop(area)
    S.save("images/output/S.jpg")
    return S


# TODO: Conduct the lateral symmetric transformation of the original image O (flip about y axis).
#       Then, let the resultant image be TO. Display the image TO on your monitor.
def flip_by_y(img):
    img_array = np.array(img)
    TO = Image.fromarray(np.fliplr(img_array))
    TO = TO.convert("L")
    TO.save("images/output/TO.jpg")
    return TO


# TODO: Multiply all the pixel values of TO by 0.8. Then, Let the resultant image be MTO.
#       Display the MTO on your monitor.
def multiply_pixels(img):
    img_array = np.array(img)
    MTO = np.multiply(img_array, 0.8)
    save_MTO = Image.fromarray(MTO)
    save_MTO = save_MTO.convert("L")
    save_MTO.save("images/output/MTO.jpg")
    return MTO


# TODO: Shift the image MTO by 3 pixel positions to the right direction of the image.
#       Then, let the image be named with SMTO. Display the image SMTO on your monitor.
def shift_to_right(img):
    img_array = np.array(img)
    SMTO = np.roll(img_array, 3, axis=1)
    SMTO[:, 0:3] = 0
    SMTO = Image.fromarray(SMTO)
    SMTO = SMTO.convert("L")
    SMTO.save("images/output/SMTO.jpg")
    return SMTO



# TODO: Save the image SMTO in your hard disk with the file name SMTO.jpg.
#       All the results displayed on your monitor should be captured and submitted.
def show_results(img_org, img_crop, img_flip, img_mult, img_shift):
    img_org.show()
    img_crop.show()
    img_flip.show()
    Image.fromarray(img_mult).show()
    img_shift.show()


if __name__ == "__main__":
    raw_image = "images/input/Fig0206.tif"

    O = read_img(raw_image)
    S = crop_img(O)
    TO = flip_by_y(O)
    MTO = multiply_pixels(TO)
    SMTO = shift_to_right(MTO)
    show_results(O, S, TO, MTO, SMTO)
