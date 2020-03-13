import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import cv2
from flashing_lights import GenerateHeatMap


def test_GetFreqCounts():
    test_ret, test_img = cv2.imreadmulti(NP_video, flags = cv2.IMREAD_GRAYSCALE)
    test_thresh = 2
    test_fn = GenerateHeatMap.GetFreqCounts(test_img[0], test_thresh)
    # Testing output size
    assert len(test_fn) == len(test_img[0]),\
    "Output is the wrong shape"
    # Testing output type
    assert type(test_fn) == np.ndarray,\
    "Output is the wrong type"
    assert np.mean(test_fn) > 0,\
    "No counts were found in test image"


def test_GetFreqArray():
    test_video = NP_video2
    test_ret, test_img = cv2.imreadmulti(test_video, flags = cv2.IMREAD_GRAYSCALE)
    test_fn = GenerateHeatMap.GetFreqArray(test_video)
    # Testing output size
    assert len(test_fn) == len(test_img[0]),\
    "Output is the wrong shape"
    # Testing output type
    assert type(test_fn) == np.ndarray,\
    "Output is the wrong type"
    assert np.mean(test_fn) > 0,\
    "No counts were found in test video"
