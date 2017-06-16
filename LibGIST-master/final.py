import numpy as np
import cv2
import matplotlib as mt
import math
import matplotlib.pyplot as plt
import subprocess
import shlex
import sys
def thresholded(center, pixels):
    out = []
    for a in pixels:
        if a >= center:
            out.append(1)
        else:
            out.append(0)
    return out

def get_pixel_else_0(l, idx, idy, default=0):
    try:
        return l[idx,idy]
    except IndexError:
        return default

def LBP(img, transformed_img):
	ln = len(img)
	ln1 = len(img[0])
	for x in range(0, ln):
	    for y in range(0, ln1):
	        center        = img[x,y]
	        top_left      = get_pixel_else_0(img, x-1, y-1)
	        top_up        = get_pixel_else_0(img, x, y-1)
	        top_right     = get_pixel_else_0(img, x+1, y-1)
	        right         = get_pixel_else_0(img, x+1, y )
	        left          = get_pixel_else_0(img, x-1, y )
	        bottom_left   = get_pixel_else_0(img, x-1, y+1)
	        bottom_right  = get_pixel_else_0(img, x+1, y+1)
	        bottom_down   = get_pixel_else_0(img, x,   y+1 )

	        values = thresholded(center, [top_left, top_up, top_right, right, bottom_right,
	                                      bottom_down, bottom_left, left])

	        weights = [1, 2, 4, 8, 16, 32, 64, 128]
	        res = 0
	        for a in range(0, len(values)):
	            res += weights[a] * values[a]

	        transformed_img.itemset((x,y), res)

	hist,mbins = np.histogram(transformed_img.flatten(),256,[0,256])
	# print(float(sum(hist)))
	new_hist = hist/float(sum(hist))
	# print(hist[0])
	# print(new_hist)
	# print(hist)
	# cdf = hist.cumsum()
	# cdf_normalized = cdf * hist.max()/ cdf.max()
	return new_hist

script = open('base.sh', 'w')
script.write('./LibGIST ' + sys.argv[1] + ' > G_feature_train')
script.write('\n')
script.write('./LibGIST ' + sys.argv[2] + ' > G_feature_test')

train_img = cv2.imread(sys.argv[1], 0)
train_transformed_img = cv2.imread(sys.argv[1], 0)
train_cdf = LBP(train_img, train_transformed_img)

test_img = cv2.imread(sys.argv[2], 0)
test_transformed_img = cv2.imread(sys.argv[2], 0)
test_cdf = LBP(test_img, test_transformed_img)

dif_array = []
for c in range(0,256):
	dif_array.append((test_cdf[c] - train_cdf[c])**2)
sm = sum(dif_array)
print("Sum of LBP EU: " + str(sm))


# print("")
# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(train_img,None) #query image
kp2, des2 = sift.detectAndCompute(test_img,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
# print(len(matches))
# Apply ratio test
good = []
for m,n in matches:
	if m.distance < 0.75*n.distance:
		good.append([m])

print("Running SIFT: (significant common features/total features):" + str(len(good)) + "/" + str(len(matches)))
img3 = cv2.drawMatchesKnn(train_img,kp1,test_img,kp2,good,test_img,flags=2)

plt.imshow(img3),plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()