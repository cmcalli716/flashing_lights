import numpy as np
import cv2
import os
from flashing_lights import GenerateHeatMap
import unittest


data_path = os.path.join(GenerateHeatMap.__path__[0], 'data')


class test_GenerateHeatMap(unittest.TestCase):

    def test_GetFreqCounts(self):
        # Get video from repo for testing
        filename = 'July_test.tif'
        test_vid = os.path.join(data_path, filename)
        test_ret, test_img = cv2.imreadmulti(test_vid,
                                             flags=cv2.IMREAD_GRAYSCALE)
        test_thresh = 5
        test_fn = GenerateHeatMap.GetFreqCounts(test_img[0], test_thresh)
        assert len(test_fn) == len(test_img[0]),\
            "Output is the wrong shape"
        # Testing output type
        assert type(test_fn) == np.ndarray,\
            "Output is the wrong type"
        assert np.mean(test_fn) > 0,\
            "No counts were found in test image"

    def test_GetFreqArray(self):
        # Get video from repo for testing
        filename = 'July_test.tif'
        test_vid = os.path.join(data_path, filename)
        test_ret, test_img = cv2.imreadmulti(test_vid,
                                             flags=cv2.IMREAD_GRAYSCALE)
        scale = 1
        test_fn = GenerateHeatMap.GetFreqArray('test.tif', scale)
        # Testing output size
        assert len(test_fn) == len(test_img[0]),\
            "Output is the wrong shape"
        # Testing output type
        assert type(test_fn) == np.ndarray,\
            "Output is the wrong type"
        assert np.mean(test_fn) > 0,\
            "No counts were found in test video"

    def test_Heatmap(self):
        # Get video from repo for testing
        filename = 'July_test.tif'
        test_vid = os.path.join(data_path, filename)
        test_img_name = 'test'
        test_img_path = '/mnt/c/Users/'
        scale = 1
        test_fn = GenerateHeatMap.Heatmap(test_vid, scale,
                                          test_img_path, test_img_name)
        # Checking to see if array used for plotting is multidimensional
        assert test_fn.ndim > 0,\
            "Wrong dimensional array used for plotting"
        # Checking to see if file is empty or not
        assert os.path.getsize(test_img_path + '/' + test_img_name) > 0,\
            "Saved file is empty."
