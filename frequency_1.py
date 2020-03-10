"""This file contains the file needed to accumulate ROI counts throughtout the file
stack and returns a frequency heat map as a image as designated by the user."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def frequency_count(file):
    """This function returns the total frequency count per the file stack. It requires
    just a file input from the user."""
    # Reading video file
    img = cv2.imread(file)
    # Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frequency = np.zeros(gray.shape[0]) #assumes image sizes are the same
    index_count = []
    for frame in range(len(gray)):
        thresh = 1
        #empty matrix to store counts
        if len(np.where(gray[frame] == thresh)) > 0: #if value exceeds threshold
            itemarray = np.where(gray[frame] >= thresh) #grab position of value
            frequency[itemarray] = 1 #adds counter of 1 in specific location relevant to image
            index_count = [itemarray]
            if frame > 0 and len(np.intersect1d(index_count, itemarray)) > 0:
        #checks if a signal in a ROI occurs and if so, can add to the frequency in that location
                overlap = np.intersect1d(index_count, itemarray)
                frequency[overlap] += 1
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
    #frequency = np.zeros(gray.shape[0]) #assumes image sizes are the same
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
