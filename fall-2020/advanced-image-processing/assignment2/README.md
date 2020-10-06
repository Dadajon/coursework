# Assignment 2

### Purpose: To practise edge detections

![zebra](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300/html/images/plain/normal/gray/253027.jpg)
![edge_zebra](https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300/html/images/human/normal/outline/gray/union/253027.jpg)

## Specifications:

## TODO
- [x] OpenCV problem

``` Python
from PIL import Image
img = Image.open('image.png').convert('LA')
img.save('greyscale.png')
```

- [ ] Test all code
- [ ] Modify variable names
- [ ] Add comments
- [ ] Generate images
- [ ] Try new images from Berkeley dataset
- [ ] Analise the results
- [ ] Prepare report 

### Discussions:
 
1. Analyze result images from three different implementation 
2. What are effects of sigma to images?
3. Does Canny Edge Detector achieve the three goals?

### Conclusions

1. ```Python cv2.filter2D() ``` is just `convolution function`
2. ```Python cv2.imread() -> cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) ``` can be replaced by ```Python np.array(Image.open(IMG_PATH).convert(mode='L')) ```

### Due date : October 6, 2020 