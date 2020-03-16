import os
import unittest

import matplotlib
import numpy as np
import cv2

import flashing_lights
from flashing_lights import GenerateHeatMap


file_name = 'July_test.tif'
data_path = os.path.join(flashing_lights.__path__[0], 'data')
test_vid = os.path.join(data_path, file_name)


class test_GenerateHeatMap(unittest.TestCase):

    def test_GetFreqCounts(self):
        """Tests GetFreqCounts functionality"""
        test_ret, test_img = cv2.imreadmulti(test_vid,
                                             flags=cv2.IMREAD_GRAYSCALE)
        # Setting Resizing Dimensions
        scale_percent = 1
        width = int(test_img[0].shape[1] * scale_percent / 100)
        height = int(test_img[0].shape[0] * scale_percent / 100)
        dim = (width, height)
        test_img_resized = cv2.resize(test_img[0], dim,
                                      interpolation=cv2.INTER_AREA)
        test_thresh = 5
        # Calling function to test
        test_fn = GenerateHeatMap.GetFreqCounts(test_img_resized, test_thresh)
        # Testing output shape
        assert len(test_fn) == len(test_img_resized),\
            "Output is the wrong shape"
        # Testing output type
        assert type(test_fn) == np.ndarray,\
            "Output is the wrong type"

    def test_GetFreqArray(self):
        """Tests GetFreqArray functionality"""
        test_ret, test_img = cv2.imreadmulti(test_vid,
                                             flags=cv2.IMREAD_GRAYSCALE)
        # Setting Resizing Dimensions
        scale_percent = 1
        width = int(test_img[0].shape[1] * scale_percent / 100)
        height = int(test_img[0].shape[0] * scale_percent / 100)
        dim = (width, height)
        test_img_resized = cv2.resize(test_img[0], dim,
                                      interpolation=cv2.INTER_AREA)
        test_thresh = 5
        test_fn = GenerateHeatMap.GetFreqArray(test_vid, test_thresh,
                                               scale_percent, outliers=False)
        # Testing output size
        assert len(test_fn) == len(test_img_resized),\
            "Output is the wrong shape"
        # Testing output type
        assert type(test_fn) == np.ndarray,\
            "Output is the wrong type"

    def test_Heatmap(self):
        """Tests heatmap functionality"""
        test_img_name = 'test'
        test_img_path = '/mnt/c/Users/'
        scale_percent = 1
        test_thresh = 5
        test_fn = GenerateHeatMap.Heatmap(test_vid, test_thresh, scale_percent,
                                          test_img_path, test_img_name,
                                          outliers=False)
        # Testing output type
        assert type(test_fn) == matplotlib.collections.QuadMesh,\
            "Output is the wrong type"
        # Checking to see if file is empty or not
        assert os.path.getsize(test_img_path +
                               test_img_name + '.png') > 0,\
            "Saved file is empty."
