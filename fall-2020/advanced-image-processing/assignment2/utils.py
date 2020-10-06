# Created by dadajonjurakuziev at 2020/10/07 12:16 AM

from PIL import Image


def array2img(arr):
    img = Image.fromarray(arr)
    img = img.convert("L")
    return img


def save_output(sobel_x, sobel_y, sobel, prewitt_x, prewitt_y, prewitt, nms, thr, canny):
    sobel_x = array2img(sobel_x)
    sobel_x.save("output/mountain/sobel_x.jpg")
    sobel_y = array2img(sobel_y)
    sobel_y.save("output/mountain/sobel_y.jpg")
    sobel = array2img(sobel)
    sobel.save("output/mountain/sobel.jpg")

    prewitt_x = array2img(prewitt_x)
    prewitt_x.save("output/mountain/prewitt_x.jpg")
    prewitt_y = array2img(prewitt_y)
    prewitt_y.save("output/mountain/prewitt_y.jpg")
    prewitt = array2img(prewitt)
    prewitt.save("output/mountain/prewitt.jpg")

    nms = array2img(nms)
    nms.save("output/mountain/nms.jpg")
    thr = array2img(thr)
    thr.save("output/mountain/thr.jpg")
    canny = array2img(canny)
    canny.save("output/mountain/canny.jpg")
