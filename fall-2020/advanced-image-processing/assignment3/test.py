# Created by dadajonjurakuziev at 2020/10/22 7:47 PM

import cv2
import matplotlib.pyplot as plt
import numpy as np

original_image_right = cv2.imread('../assignment3/images/painting1.jpg')
gray_img_right = cv2.cvtColor(original_image_right, cv2.COLOR_BGR2GRAY)

original_image_left = cv2.imread('../assignment3/images/painting3.jpg')
gray_img_left = cv2.cvtColor(original_image_left, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(gray_img_right, None)
kp2, des2 = sift.detectAndCompute(gray_img_left, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# print matches
# Apply ratio test
good = []
for m in matches:
    if m[0].distance < 0.5 * m[1].distance:
        good.append(m)
matches = np.asarray(good)

if len(matches[:, 0]) >= 4:
    src = np.float32([kp1[m.queryIdx].pt for m in matches[:, 0]]).reshape(-1, 1, 2)
    dst = np.float32([kp2[m.trainIdx].pt for m in matches[:, 0]]).reshape(-1, 1, 2)

    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
    print(H)
else:
    raise AssertionError("Can't find enough keypoints.")

dst = cv2.warpPerspective(original_image_right, H, (original_image_left.shape[1] + original_image_right.shape[1], original_image_left.shape[0]))
plt.subplot(122), plt.imshow(dst), plt.title('Warped Image')
plt.show()
plt.figure()
dst[0:original_image_left.shape[0], 0:original_image_left.shape[1]] = original_image_left
cv2.imwrite('resultant_stitched_panorama_tower.jpg', dst)
plt.imshow(dst)
plt.show()
cv2.imwrite('resultant_stitched_panorama_tower.jpg', dst)
