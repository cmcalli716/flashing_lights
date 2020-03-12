"""This file contains the file needed to accumulate ROI counts throughtout the file
stack and returns a frequency heat map as a image as designated by the user."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def frequency_count(file):
    # Reading video file and convert to grayscale
ret, img = cv2.imreadmulti(file, flags = cv2.IMREAD_GRAYSCALE)
    frequency = np.zeros(np.shape(img[0])) #assumes image sizes are the same
    #indexes what rows and cols pixels show events
    index_count_row = []
    index_count_col = []
    for frame in range(len(img)):
        frame_std = np.std(img[frame])*3
        frame_mean = np.mean(img[frame])
        #calculates threshold based on noise using mean and std
        thresh = frame_mean + frame_std
        if len(np.where(img[frame] == thresh)) > 0: #if value exceeds threshold
            #grab row and column position where value>thresh occurs
            row, col = np.where(img[frame] >= thresh)
            for i in range(len(row)):
            #loop over based on the number of pixels above threshold
                frequency[row[i], col[i]] = 1 #adds counter of 1 w.r.t pixel location
                index_count_row = row[i] #stores location for reference
                index_count_col = col[i]
            if frame > 0 and len(np.intersect1d(index_count_row, row)) > 0 and len(np.intersect1d(index_count_col, col)) > 0:
            #checks if a signal in a ROI occurs again
                overlap_row = np.intersect1d(index_count_row, row)
                #finds where it overlaps
                overlap_col = np.intersect1d(index_count_col, col)
                #iterates by # of overlapping times and adds count to pixel spot
                if len(overlap_row) >= 1 and len(overlap_col) >= 1:
                    for j in range(len(overlap_row)):
                        frequency[overlap_row[j], overlap_col[j]] += 1
                else:
                    pass
            else:
                pass
        else:
            pass
    return frequency

def heatmap(file, savefig, path):
    """This function creates a heatmap based on the observed frequency count
    of Fluorscence events observed. It intakes a file. The user can choose
    where they want to save the image and what its labeled as in their computer."""
# Reading video file
    ret, img = cv2.imreadmulti(file, flags = cv2.IMREAD_GRAYSCALE)
    #x and y range determined by size of frame in both directions
    pixel_X = np.arange(0, len(img[0]), 1)
    pixel_Y = np.arange(0, len(img[0]), 1)
    #reshape according to size of one frame
    pixel_z = frequency_values.reshape(len(img[0]), len(img[0]))
    #rectilinear grid choice
    plt.pcolormesh(pixel_X, pixel_Y, pixel_z, cmap = 'magma')
    plt.xlabel('Pixel Count')
    plt.ylabel('Pixel Count')
    plt.title('Frequency Heat Map')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Frequency')
    #plt.show() #uncomment if plot wants to be seen
    #picture is saved in file location designated by user
    plt.savefig(path + '/' + savefig +'.png', bbox_inches='tight')
