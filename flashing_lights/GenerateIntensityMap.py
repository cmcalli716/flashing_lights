import numpy as np
import matplotlib.pyplot as plt
import cv2


def GetIntensityValues(frame, threshold):
    """Searches through an image to find greyscale pixels above a certain
    brightness threshold. If pixels of sufficient brightness are present
    within the image the coordinates of the pixel are stored and the
    brightness is added to an empty array

    Inputs:

    - frame: ndarray of pixels (image file or video frame)
    - threshold: minimum brightness for an event detection

    Output: an ndarray of intensity values for
    pixels above the brightness threshold in the frame

    """
    # Generating empty matrix for coordinate assignment
    intensities = np.zeros(np.shape(frame))
    # Generating index lists to keep track of ROI coordinates
    index_count_row = []
    index_count_col = []
    # Looks through matrix for points above a brightness threshold
    if len(np.where(frame >= threshold)) > 0:
        # Finding coordinates of brightness events
        row, col = np.where(frame >= threshold)
        for i in range(len(row)):
            for j in range(len(col)):
                # Adds intensity value in the position of the
                # given brightness event
                intensities[row[i], col[j]] = frame[row[i], col[j]]
                index_count_row.append(row[i])
                index_count_col.append(col[j])
    else:
        pass
    return intensities


def GetIntensityArray(videofile):
    """Finds pixel coordinates within a videofile (.tif, .mp4) for pixels
    that are abovea calculated brightness threshold, then accumulates the
    brightness event intensities for each coordinate,
    outputting it as a 2-D array in the same size as the video frames

    Input:
    -videofile: file containing an image stack of fluorescent events

    Output: 2-d Array of accumulated intensity values for each pixel above
    a calculated brightness threshold in the video"""
    # Reading video file and convert to grayscale
    ret, img = cv2.imreadmulti(videofile, flags=cv2.IMREAD_GRAYSCALE)
    # Creating empty array to add frequency counts to
    int_array = np.zeros(np.shape(img[0]))
    # Looking through each frame to get the frequency counts
    for frame in range(len(img)):
        # Setting threshold using mean and stdev of pixel brightness
        mean = np.mean(img[frame])
        std = np.std(img[frame])
        threshold = mean + 3*std
        intensity = GetIntensityValues(img[frame], threshold)
        if len(np.where(intensity >= 1)) > 0:
            # Get coordinates of the single pixel counts
            row, col = np.where(intensity >= 1)
            for i in range(len(row)):
                for j in range(len(col)):
                    # Add single count to freq_array in location of event
                    int_array[row[i], col[j]] += intensity[row[i], col[j]]
        else:
            pass
    return int_array


def IntensityMap(videofile, img_path, img_name):
    """Takes intensity accumulation array from
    GenerateIntensityMap.GetIntensityArray() and plots it as
    a colored meshgrid.

    Yellow pixels are at max intensity, blue pixels are
    minimum intensity (cmap = 'plasma')"""
    # Reading video file
    ret, img = cv2.imreadmulti(videofile, flags=cv2.IMREAD_GRAYSCALE)
    # obtaining frequency array
    z = GetIntensityArray(videofile)
    # Generating x and y axes in shape of image frame
    pixel_X = np.arange(0, len(img[0]), 1)
    pixel_Y = np.arange(0, len(img[0]), 1)
    # Mapping intensity array onto the x and y axes
    fig = plt.pcolormesh(pixel_X, pixel_Y, z, cmap='plasma')
    plt.xlabel('Pixel Count')
    plt.ylabel('Pixel Count')
    plt.title('Intensity Map')
    # picture is saved in file location designated by user
    plt.savefig(img_path + '/' + img_name + '.png', bbox_inches='tight')
    return fig
