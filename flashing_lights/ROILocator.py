import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import skimage
import skimage.io as sio
from skimage.feature import blob_dog
import cv2
import os


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
            graylist.append(skimage.color.rgb2gray(img[i, :]))
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
    for i in range(len(img)):
        gmax = np.amax(img[i, :])
        gmin = np.amin(img[i, :])
        maxlist.append(gmax)
        minlist.append(gmin)
    graymax = np.asarray(maxlist).max()
    graymin = np.asarray(minlist).min()
    # Set up zero function to create a zero array to store output
    # and maintain the shape.
    norm_gray = np.zeros(img.shape)
    # Iterate through the file length to normalize the pixel value
    # from 0 to 255.
    for i in range(len(img)):
        norm_gray[i, :] = ((img[i, :] - graymin) / (graymax - graymin)) * 255
    # Find and output the mean value and standard deviation of normalized
    # images as a parameter in ROI locator function.
    norm_gray_mean = []
    norm_gray_std = []
    for i in range(len(norm_gray)):
        norm_gray_mean.append(np.asarray(norm_gray[i]).mean())
        norm_gray_std.append(np.asarray(norm_gray[i]).std())
    return norm_gray, norm_gray_mean, norm_gray_std


def diff_of_gauss(norm_gray, ngraymean, ngraystd, mean, std, overlap):
    """Uses difference of Gaussian to determine where a region of interest lies
    within an image.

    Input: Image or frame of video

    Output: List of ROI parameters"""
    # Set empty list to store output.
    roi = []
    for i in range(len(norm_gray)):
        # Use blob_dog function from skimage.feature to capture ROI
        # based on local maximum brightness.
        roi.append(blob_dog(norm_gray[i, :], max_sigma=30,
                   threshold=mean * ngraymean[i] + std
                   * ngraystd[i], overlap=overlap))
    return roi


def ROI_counting(roi, length):
    """Counts the accumulative ROIs from first frame to imput frame.

    Input: Result of diff_of_gauss(), length of frame.

    Output: ROI counts."""
    # Initial count for first frame.
    roi_count = len(roi[0])
    index_list = []
    for i in range(1, length + 1):
        # Count the ROIs that appear frame by frame.
        # If the ROI amount increases over the frame,
        # calculate how many ROI appears.
        # Set a if loop to prevent index being out of bound.
        if i == 0:
            break
        elif len(roi[i - 1]) < len(roi[i]):
            roi_count += len(roi[i]) - len(roi[i - 1])
        # If the ROI amounts are same between two frames, check
        # if there's different ROI.
        #
        # Store the index number for the frames which have
        # the same amount of ROI as previous frame.
        elif len(roi[i - 1]) == len(roi[i]):
            index_list.append(i)
    # Set up a loop for finding if there is different ROI between two
    # frames that have same amount of ROI.
    for i in index_list:
        # A count that is used only in the loop, counting the amount
        # of identical ROI between two frames.
        roi_count_d = 0
        for j in range(len(roi[i - 1])):
            for k in range(len(roi[i])):
                # Find how many identical ROI there are between two frames.
                # ROIs are consider to be the same if the distance between
                # them are less than 2 pixels.
                pos1 = np.asarray([roi[i - 1][j][0], roi[i - 1][j][1]])
                pos2 = np.asarray([roi[i][k][0], roi[i][k][1]])
                distance = np.linalg.norm(pos1 - pos2)
                if distance <= 2:
                    roi_count_d += 1
        # Adding the amount of different ROI within two frames
        # that have same amount of ROI.
        roi_count += len(roi[i]) - roi_count_d
    return roi_count


def ROI_counting_list(img, roi):
    """Creates ROI count list.

    Input: Greyscaled image or frame of video, result of diff_of_gauss().

    Output: List of ROI counts."""
    roi_count_list = []
    length = len(img)
    # Calculate the accumulative ROIs that appear from
    # 1st frame to certain frame.
    for i in range(0, length):
        roi_count_list.append(ROI_counting(roi, i))
    return roi_count_list


def plot_and_save(img, path_of_directory, roi, roi_count_list):
    """Plots the images with ROI patches and save to local directory.

    Input: Image or frame of video, path of desired working directory,
    output of ROI_counting_list().

    Output: List of path to saved images."""
    file_name = []
    # Turn the interactive mode off to avoid showing plots when running.
    plt.ioff()
    length = len(img)
    # Plot the image with patched ROI.
    for i in range(0, length):
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.imshow(img[i], cmap=matplotlib.cm.gray)
        # Show the accumulative ROIs on title.
        ax.set_title('Total count of ROI: {}'.format(roi_count_list[i]),
                     fontsize=20)
        for j in range(len(roi[i])):
            y, x, r = roi[i][j]
            # Area of ROI are set to 20x for better visualization.
            c = patches.Circle((x, y), r * np.sqrt(20),
                               color='r', linewidth=0.8, fill=False)
            ax.add_patch(c)
        # Save the plotted figures to assigned path of directory.
        fig.savefig(path_of_directory + '/img{}.png'.format(i))
        # Create the list of file name for later use.
        file_name.append(path_of_directory + '/' + 'img{}.png'.format(i))
        plt.close(fig)
    # Turn the interactive mode back on.
    plt.ion()
    return file_name


def video_writer(file_name, path_of_directory):
    """Creates video from saved plots.

    Input: List of path to saved images, path of desired working directory.

    Output: Path to saved video."""
    # Determine the width and height from the first image
    frame = cv2.imread(file_name[0])
    height, width, channels = frame.shape
    # Give fourcc argument to openCV.
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    out = cv2.VideoWriter(path_of_directory + '/output.avi', fourcc, 20.0,
                          (width, height))
    # Write the highlighted images into created video file frame by frame.
    for image in file_name:
        image_path = image
        frame = cv2.imread(image_path)
        out.write(frame)
    # Remove the image files.
    for file in file_name:
        os.remove(file)
    print('The output video is {}'.format(path_of_directory + '/output.avi'))
    return path_of_directory + '/output.avi'


def ROI_locator(path, path_of_directory, mean, std, overlap):
    """Wrapped functions.

    Input: path to videofile, path of desired working directory.

    Output: Path to saved video."""
    # Run gray_scaler function to obtain grayscale image as numpy array.
    gray = gray_scaler(path)
    # Normalize the image with value from 0 to 255.
    norm_gray, ngraymean, ngraystd = img_normalizer(gray)
    # Run diff_of_gauss function to obtain list of ROI.
    roi = diff_of_gauss(norm_gray, ngraymean, ngraystd, mean, std, overlap)
    # Create ROI count list
    roi_count_list = ROI_counting_list(norm_gray, roi)
    # Save images with ROI-patch.
    file_name = plot_and_save(norm_gray, path_of_directory,
                              roi, roi_count_list)
    # Convert the saved images into video, and delete the images.
    video_path = video_writer(file_name, path_of_directory)
    return video_path
