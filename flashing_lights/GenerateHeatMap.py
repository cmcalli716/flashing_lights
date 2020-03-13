"""Group of functions which produce heatmap of accumulated frequency counts.
To run these functions the user will need a videofile (.tif format), as well
as a desired brightness threshold. Within FreqHeatmap_example.ipynb there is an
example of setting the brightness threshold using the mean brightness of the
image.

WARNING: Extremely large video files (>1500 frames) or videos with
high pixel resolution (512x512 array or greater) may take a couple of
minutes to run depending on your computer's processing power."""
import numpy as np
import cv2

def GetFreqCounts(frame, threshold):
    """Searches through an image to find greyscale pixels above a certain
    brightness threshold. If counts of sufficient brightness are present
    within the

    Inputs: ndarray (image), threshold value (int or float)

    Output: an ndarray of boolean values describing which
    pixels were above the brightness threshold in the frame"""
    # Generating empty matrix for coordinate assignment
    frequency = np.zeros((len(frame), len(frame)))
    # Generating index lists to keep track of ROI coordinates
    index_count_row = []
    index_count_col = []
    # Looks through matrix for points above a brightness threshold
    if len(np.where(frame == threshold)) > 0:
        # Finding coordinates of brightness events
        row, col = np.where(frame >= threshold)
        for i in range(len(row)):
            # Adds a value of 1 to the frequency output in the position of the
            # given brightness event
            frequency[row[i], col[i]] = 1
            index_count_row.append(row[i])
            index_count_col.append(col[i])
    else:
        pass
    return frequency
