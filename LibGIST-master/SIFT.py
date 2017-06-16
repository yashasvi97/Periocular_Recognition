import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('/home/yashasvi/Desktop/BTAS_2010/UBIris_v2/C1_S1_I4.tiff',0)          # queryImage
img2 = cv2.imread('/home/yashasvi/Desktop/BTAS_2010/UBIris_v2/C1_S1_I15.tiff',0) # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None) #query image
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
print(len(matches))
# Apply ratio test
good = []
for m,n in matches:
	if m.distance < 0.75*n.distance:
		good.append([m])

print(len(good))
# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,img1,flags=2)

plt.imshow(img3),plt.show()