# PySIFT

This project contains an implementation of the SIFT keypoint extraction algorithm in Python. For a detailed explanation, visit the following [blog post](https://medium.com/@lerner98/implementing-sift-in-python-36c619df7945).

## Usage

Pass in a filename for the `--input` argument and a prefix for the `--output` parameter. In addition to plotting the keypoints, `main.py` will save `results/<prefix>_kp_pyr.pkl` and `results/<prefix>_feats_pyr.pkl` files containing the computed features.

## Warning

I do not maintain this repository. The code is provided as-is, so if you encounter an issue (which is likely) I would advise you to try and fix it yourself.

Also, if anyone wants to maintain this repository, leave an issue and I will gladly add you as a collaborator or transfer ownership.

## Limitations 

The code is unoptimized. This means that I took time to implement each step of SIFT as described in the paper as faithfully as I could but I did not do a second pass over the implementation for optimization. Therefore, on any reasonably-sized image, it should be fairly slow.

In addition, there is currently a mistake in the keypoint scaling. When scaled up from the higher levels of the pyramid, they get off center. This can be seen in the following example:

![example](example.png)


# Assignment 3

### Purpose: To play with SIFT

We discussed the basic principles of scale invariant features, called SIFT. It is very useful image descriptor. You need to understand how it works through step by step. 

### Specifications: 

1. Write SIFT code, which extracts descriptor. In fact you can see many SIFT implementation and I also found one at https://github.com/SamL98/PySIFT. You are welcome to use the already-available code.
2. Describe your code (or public code) how each step works in your document.
3. Write a simple utility program that searches matched images from gallery images. A sample gallery will be unloaded soon.

### Discussions: 

1. Describe each steps in SIFT
2. What are rules to detect keypoints?
3. How does SIFT works for different scale and orientation?
4. How can you improve the public code, if you borrow one?

### Submission

Hand in : Turn in your completed document to eiprof@naver.com. Your document include ①Problem description, ②Source codes with full of comments, ③Results (screen capture), ④Analysis report, and ⑤Others (such as references) in order. The email title should be 'IP Your_Name HakBeon(student id number) Proj_number' 

### Deadline

Due date : October 20, 2020
