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


def GetIntensityArray(videofile, threshold, scale_percent):
    """Finds pixel coordinates within a videofile (.tif, .mp4) for pixels
    that are above a brightness threshold, then accumulates the
    brightness event intensities for each coordinate,
    outputting it as a 2-D array in the same size as the video frames

    Input:
    -videofile: file containing an image stack of fluorescent events
    -threshold: minimum brightness for detection
    -scale_percent: helps resize image for faster computing speeds

    Output: 2-d Array of accumulated intensity values for each pixel above
    a calculated brightness threshold in the video"""
    # Reading video file and convert to grayscale
    ret, img = cv2.imreadmulti(videofile, flags=cv2.IMREAD_GRAYSCALE)
    # Setting Resizing Dimensions
    width = int(img[0].shape[1] * scale_percent / 100)
    height = int(img[0].shape[0] * scale_percent / 100)
    dim = (width, height)
    img_resized = cv2.resize(img[0], dim, interpolation=cv2.INTER_AREA)
    # Creating empty array to add intensity values to
    int_array = np.zeros(np.shape(img_resized))
    for frame in range(len(img)):
        # Resize Frame
        frame_resized = cv2.resize(img[frame],
                                   dim, interpolation=cv2.INTER_AREA)
        intensity = GetIntensityValues(frame_resized, threshold)
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


def IntensityMap(videofile, threshold, scale_percent, img_path, img_name):
    """Takes intensity accumulation array from
    GenerateIntensityMap.GetIntensityArray() and plots it as
    a colored meshgrid.

    Yellow pixels are at max intensity, blue pixels are
    minimum intensity (cmap = 'plasma')"""
    # Reading video file
    ret, img = cv2.imreadmulti(videofile, flags=cv2.IMREAD_GRAYSCALE)
    # obtaining frequency array
    z = GetIntensityArray(videofile, threshold, scale_percent)
    # Generating x and y axes in shape of image frame
    width = int(img[0].shape[1] * scale_percent / 100)
    height = int(img[0].shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    frame_resized = cv2.resize(img[0], dim, interpolation=cv2.INTER_AREA)
    pixel_X = np.arange(0, frame_resized.shape[1])
    pixel_Y = np.arange(0, frame_resized.shape[0])
    # Mapping intensity array onto the x and y axes
    fig = plt.pcolormesh(pixel_X, pixel_Y, z, cmap='plasma')
    plt.xlabel('Pixel Count')
    plt.ylabel('Pixel Count')
    plt.title('Intensity Map')
    # picture is saved in file location designated by user
    plt.savefig(img_path + '/' + img_name + '.png', bbox_inches='tight')
    return fig
