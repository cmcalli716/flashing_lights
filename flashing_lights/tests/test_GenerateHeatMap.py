import os
import unittest

import matplotlib
import numpy as np
import cv2

import flashing_lights
from flashing_lights import GenerateHeatMap


file_name1 = 'July_test.tif'
data_path = os.path.join(flashing_lights.__path__[0], 'data')
test_vid1 = os.path.join(data_path, file_name1)


class test_GenerateHeatMap(unittest.TestCase):

    def test_GetFreqCounts(self):
        """Tests GetFreqCounts functionality"""
        test_ret, test_img = cv2.imreadmulti(test_vid1,
                                             flags=cv2.IMREAD_GRAYSCALE)
        # Setting Resizing Dimensions
        scale_percent = 1
        width = int(test_img[0].shape[1] * scale_percent / 100)
        height = int(test_img[0].shape[0] * scale_percent / 100)
        dim = (width, height)
        test_img_resized = cv2.resize(test_img[0], dim,
                                      interpolation=cv2.INTER_AREA)
        test_thresh = 3
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
        test_ret, test_img = cv2.imreadmulti(test_vid1,
                                             flags=cv2.IMREAD_GRAYSCALE)
        # Setting Resizing Dimensions
        scale_percent = 1
        width = int(test_img[0].shape[1] * scale_percent / 100)
        height = int(test_img[0].shape[0] * scale_percent / 100)
        dim = (width, height)
        test_img1_resized = cv2.resize(test_img[0], dim,
                                       interpolation=cv2.INTER_AREA)
        test_thresh = 3
        test_fn1 = GenerateHeatMap.GetFreqArray(test_vid1, test_thresh,
                                                scale_percent, outliers=False)
        test_fn2 = GenerateHeatMap.GetFreqArray(test_vid1, test_thresh,
                                                scale_percent, outliers=True)
        # Testing output size
        assert len(test_fn1) == len(test_img1_resized),\
            "Output1 is the wrong shape"
        assert len(test_fn2) == len(test_img1_resized),\
            "Output2 is the wrong shape"
        # Testing output type
        assert type(test_fn1) == np.ndarray,\
            "Output1 is the wrong type"
        assert type(test_fn2) == np.ndarray,\
            "Output2 is the wrong type"

    def test_Heatmap(self):
        """Tests heatmap functionality"""
        test_img_name = 'test'
        test_img_path = '.'
        scale_percent = 1
        test_thresh = 3
        test_fn1 = GenerateHeatMap.Heatmap(test_vid1, test_thresh,
                                           scale_percent, test_img_path,
                                           test_img_name, outliers=False)
        test_fn2 = GenerateHeatMap.Heatmap(test_vid1, test_thresh,
                                           scale_percent, test_img_path,
                                           test_img_name, outliers=True)
        # Testing output type
        assert type(test_fn1) == matplotlib.collections.QuadMesh,\
            "Output1 is the wrong type"
        assert type(test_fn2) == matplotlib.collections.QuadMesh,\
            "Output2 is the wrong type"
