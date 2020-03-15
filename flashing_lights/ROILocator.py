import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import skimage
import skimage.io as sio
from skimage.feature import blob_dog
import cv2


def gray_scaler(path):
    """Converts videofile to greyscale.

    Input: path to videofile

    Output: Greyscale video"""
    img = sio.imread(path)
    # Read image file with skimage.io.
    if len(img) > 1:
    # If the image file is multiple page, treat the first column as page.
        graylist = []
        # Empty list to store output.
        # Iterate through the length of the file.
        for i in range(len(img)):
            # Append the grayscale result into empty list.
            graylist.append(skimage.color.rgb2gray(img[i,:]))
        # Turn the output into numpy array.
        gray = np.asarray(graylist)
    # If the image file is single page, directly use the skimage
    # built-in rgb2gray function.
    else:
        gray = skimage.color.rgb2gray(img)

    return gray

def img_normalizer(img):
    """Normalizes pixel brightness within an image to 255.

    Input: Image or frame of video

    Output: Normalized array, mean of normalized array and standard deviation,
    and integer list of the normalized array."""
    # Set empty lists to store output.
    maxlist = []
    minlist = []
    # Iterate through the file length to find the
    # maximum and minimum within the file.
    for i in range(len(gray)):
        gmax = np.amax(gray[i,:])
        gmin = np.amin(gray[i,:])
        maxlist.append(gmax)
        minlist.append(gmin)
    graymax = np.asarray(maxlist).max()
    graymin = np.asarray(minlist).min()
    # Set up zero function to create a zero array to store output
    # and maintain the shape.
    norm_gray = np.zeros(gray.shape)
    # Iterate through the file length to normalize the pixel value
    # from 0 to 255.
    for i in range(len(gray)):
        norm_gray[i, :] = ((gray[i, :] - graymin) / (graymax - graymin)) * 255
    # Find and output the mean value and standard deviation of normalized
    # images as a parameter in ROI locator function.
    norm_gray_mean = []
    norm_gray_std = []
    for i in range(len(norm_gray)):
        norm_gray_mean.append(np.asarray(norm_gray[i]).mean())
        norm_gray_std.append(np.asarray(norm_gray[i]).std())
    # Output the uint16 data type for later usage.
    ngray = norm_gray.astype('uint16')
    return norm_gray, norm_gray_mean, norm_gray_std, ngray


def diff_of_gauss(img):
    """Uses difference of Gaussian to determine where a region of interest lies
    within an image.

    Input: Image or frame of video

    Output: List of ROI parameters"""
    # Run normalizer function to get the output.
    norm_gray, ngraymean, ngraystd, ngray = img_normalizer(img)
    # Set empty list to store output.
    roi = []
    for i in range(len(norm_gray)):
        # Use blob_dog function from skimage.feature to capture ROI
        # based on local maximum brightness.
        roi.append(blob_dog(norm_gray[i, :], max_sigma=30,
            threshold = ngraymean[i] + 3 * ngraystd[i], overlap = 0.1))
    return roi


def ROI_counting(roi, length):
    # Initial count for first frame.
    roi_count = len(roi[0])
    index_list = []
    for i in range(0, length):
        # Count the ROIs that appear frame by frame.
        # If the ROI amount increases over the frame,
        # calculate how many ROI appears.
        # Set a if loop to prevent index being out of bound.
        if i == length - 1:
            break
        elif len(roi[i]) < len(roi[i + 1]):
            roi_count += len(roi[i + 1]) - len(roi[i])
        # If the ROI amounts are same between two frames, check
        # if there's different ROI.
        #
        # Store the index number for the frames which have
        # the same amount of ROI as previous frame.
        elif len(roi[i]) == len(roi[i + 1]):
            index_list.append(i)
    # Set up a loop for finding if there is different ROI between two
    # frames that have same amount of ROI.
    for i in index_list:
        # A count that is used only in the loop, counting the amount
        # of identical ROI between two frames.
        roi_count_d = 0
        for j in range(len(roi[i])):
            for k in range(len(roi[i + 1])):
                # Find how many identical ROI there are between two frames.
                if [roi[i][j][0], roi[i][j][1]] == [roi[i + 1][k][0],\
 roi[i + 1][k][1]]:
                    roi_count_d += 1
        # Adding the amount of different ROI within two frames
        # that have same amount of ROI
        roi_count += len(roi[i]) - roi_count_d
    return roi_count
