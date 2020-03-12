"""This file contains the file needed to accumulate ROI counts throughtout the file
stack and returns a frequency heat map as a image as designated by the user."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def frequency_count(file):
    # Reading video file and convert to grayscale
    ret, img = cv2.imreadmulti(file, flags = cv2.IMREAD_GRAYSCALE)
    frequency = np.zeros(np.shape(img[0])) #assumes image sizes are the same
    index_count_row = []
    index_count_col = []
    for frame in range(len(img)):
        frame_std = np.std(img[frame])*3 #calculates threshold based on noise
        frame_mean = np.mean(img[frame])
        thresh = frame_mean + frame_std
        #empty matrix to store counts
        if len(np.where(img[frame] == thresh)) > 0: #if value exceeds threshold
            row, col = np.where(img[frame] >= thresh) #grab position of value
            for i in range(len(row)):
                frequency[row[i], col[i]] = 1 #adds counter of 1 in specific location relevant to image
                index_count_row = row[i]
                index_count_col = col[i]
            if frame > 0 and len(np.intersect1d(index_count_row, row)) > 0 and len(np.intersect1d(index_count_col, col)) > 0:
        #checks if a signal in a ROI occurs and if so, can add to the frequency in that location
                overlap_row = np.intersect1d(index_count_row, row)
                overlap_col = np.intersect1d(index_count_col, col)
                if len(overlap_row) > 1 and len(overlap_col) > 1:
                    for j in len(overlap_row):
                        frequency[overlap_row[j], overlap_col[j]] += 1
                elif len(overlap_row) == 1 and len(overlap_col) == 1:
                    frequency[overlap_row[0], overlap_col[0]] += 1
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
    frequency_values = frequency_count(file)
    # Reading video file
    img = cv2.imread(file)
    # Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    pixel_x = np.linspace(0, len(gray), 32) #pixel limit set by conversion
    pixel_y = np.linspace(0, len(gray), 16)
    frequency_z = frequency_values.reshape(len(pixel_y), len(pixel_x)) #reshape to x,y
    pixel_xx, pixel_yy = np.meshgrid(pixel_x, pixel_y)
    #rectilinear grid choice
    plt.pcolormesh(pixel_xx, pixel_yy, frequency_z, cmap='magma')
    plt.xlabel('Pixel Count')
    plt.ylabel('Pixel Count')
    plt.title('Frequency Heat Map')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Frequency')
    #plt.show() #uncomment if plot wants to be seen
    #picture is saved in file location designated by user
    plt.savefig(path + '/' + savefig +'.png', bbox_inches='tight')
