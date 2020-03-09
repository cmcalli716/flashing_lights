import cv2
import numpy as np

def single_image_count(file):
    # Reading video file
    img = cv2.imread(file)
    # Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frequency = np.zeros(gray.shape[0])
    #empty matrix to store counts
    sd_brightness = np.std(gray[230])
    thresh = sd_brightness * 5
    if np.where(gray[220]>=thresh) != []: #if value exceeds threshold
        itemarray = np.where(gray[230]>=thresh) #grab position of value
        frequency[itemarray] = 1 #adds counter of 1 in specific location relevant to image
    else:
        pass
    return frequency
