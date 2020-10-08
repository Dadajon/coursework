# Created by dadajonjurakuziev at 2020/10/07 12:16 AM

from PIL import Image


def array2img(arr):
    img = Image.fromarray(arr)
    img = img.convert("L")
    return img


def save_output(folder, sobel_x, sobel_y, sobel, prewitt_x, prewitt_y, prewitt, nms, thr, canny):
    folder_name = folder

    sobel_x = array2img(sobel_x)
    sobel_x.save("output/"+folder_name+"/sobel_x.jpg")
    sobel_y = array2img(sobel_y)
    sobel_y.save("output/"+folder_name+"/sobel_y.jpg")
    sobel = array2img(sobel)
    sobel.save("output/"+folder_name+"/sobel.jpg")

    prewitt_x = array2img(prewitt_x)
    prewitt_x.save("output/"+folder_name+"/prewitt_x.jpg")
    prewitt_y = array2img(prewitt_y)
    prewitt_y.save("output/"+folder_name+"/prewitt_y.jpg")
    prewitt = array2img(prewitt)
    prewitt.save("output/"+folder_name+"/prewitt.jpg")

    nms = array2img(nms)
    nms.save("output/"+folder_name+"/nms.jpg")
    thr = array2img(thr)
    thr.save("output/"+folder_name+"/thr.jpg")
    canny = array2img(canny)
    canny.save("output/"+folder_name+"/canny.jpg")
