# Periocular Recognition 
This is a project I worked in my free time, for getting started with biometrics and image processing in general.
## What is the periocular region
Periocular region is the region in the periphery of the eyes, that is, the eyes and eyebrow region. 
This region can be used to determine the identity of an individual. 
It can be used to augment face recognition and as well as aid person identification when the face is obscured like wearing a scarf or a helmet. 

![alt Face](https://raw.githubusercontent.com/yashasvi97/Periocular_Recognition/master/Face.png)
![alt Face](https://raw.githubusercontent.com/yashasvi97/Periocular_Recognition/master/perioc.png)
 
 
## Feature Extraction
So given the periocular image of the subject, we need a compact representation of the image. In literature feature extractor like: 
1. Local Binary Pattern(LBP). 
2. Histogram of Oriented Gradients(HOG). 
3. Scale Invariant Feature Transform(SIFT). 
 
have performed to be good for the periocular region. 
So given an image I extracted 3 different representations of the same image. 

## Recognition
For respective feature space I found the similarity score with each of the images in the probe for every gallery. 
So essentially I have a LBP score as 
```
sLBP[i, j] = LBP(gallery[i]) - LBP(probe[j]) for all j 
```
where LBP() is a function which gives LBP feature vector for an input image. Similarly I have sHOG and sSIFT. So final similarity score is calculated for a pair (i, j) as:- 
```
s(i, j) = 1/3 * sLBP[i, j] + 1/3 * sHOG[i, j] + 1/3 * sSIFT[i, j]
```
For a given subject i, he/she is classified as subject j if s[i, j] is the least in all j. 

