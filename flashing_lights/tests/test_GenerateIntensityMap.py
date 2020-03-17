import os
import unittest

import matplotlib
import numpy as np
import cv2

import flashing_lights
from flashing_lights import GenerateIntensityMap


file_name = 'July_test.tif'
data_path = os.path.join(flashing_lights.__path__[0], 'data')
test_vid = os.path.join(data_path, file_name)


class test_GenerateIntensityMap(unittest.TestCase):

    def test_GetIntensityValues(self):
        assert os.stat(test_vid).st_size > 0,\
            "File is empty"
        test_ret, test_img = cv2.imreadmulti(test_vid,
                                             flags=cv2.IMREAD_GRAYSCALE)
        # Setting Resizing Dimensions
        scale_percent = 1
        width = int(test_img[0].shape[1] * scale_percent / 100)
        height = int(test_img[0].shape[0] * scale_percent / 100)
        dim = (width, height)
        self.assertNotIn(0, dim, msg="Invalid dimensions")
        test_img_resized = cv2.resize(test_img[0], dim,
                                      interpolation=cv2.INTER_AREA)
        test_thresh1 = 5
        test_thresh2 = 50000
        test_fn1 = GenerateIntensityMap.GetIntensityValues(test_img_resized,
                                                           test_thresh1)
        test_fn2 = GenerateIntensityMap.GetIntensityValues(test_img_resized,
                                                           test_thresh2)
        # Testing output size
        assert test_fn1.ndim > 0,\
            "Output1 dimensionality is incorrect"
        assert test_fn2.ndim > 0,\
            "Output2 dimensionality is incorrect"
        assert len(test_fn1) == len(test_img_resized),\
            "Output1 is the wrong shape"
        assert len(test_fn2) == len(test_img_resized),\
            "Output2 is the wrong shape"
        # Testing output type
        assert type(test_fn1) == np.ndarray,\
            "Output1 is the wrong type"
        assert type(test_fn2) == np.ndarray,\
            "Output2 is the wrong type"

    def test_GetIntensityArray(self):
        assert os.stat(test_vid).st_size > 0,\
            "File is empty"
        test_ret, test_img = cv2.imreadmulti(test_vid,
                                             flags=cv2.IMREAD_GRAYSCALE)
        # Setting Resizing Dimensions
        scale_percent = 1
        width = int(test_img[0].shape[1] * scale_percent / 100)
        height = int(test_img[0].shape[0] * scale_percent / 100)
        dim = (width, height)
        # Checking for valid dimensions
        self.assertNotIn(0, dim, msg="Invalid dimensions")
        test_img_resized = cv2.resize(test_img[0], dim,
                                      interpolation=cv2.INTER_AREA)
        test_thresh1 = 5
        test_thresh2 = 50000
        test_fn1 = GenerateIntensityMap.GetIntensityArray(test_vid,
                                                          test_thresh1,
                                                          scale_percent)
        test_fn2 = GenerateIntensityMap.GetIntensityArray(test_vid,
                                                          test_thresh2,
                                                          scale_percent)
        # Testing output size
        assert test_fn1.ndim > 0,\
            "Output 1 has incorrect dimensionality"
        assert test_fn2.ndim > 0,\
            "Output 2 has incorrect dimensionality"
        assert len(test_fn1) == len(test_img_resized),\
            "Output1 is the wrong shape"
        assert len(test_fn2) == len(test_img_resized),\
            "Output2 is the wrong shape"
        # Testing output type
        assert type(test_fn1) == np.ndarray,\
            "Output1 is the wrong type"
        assert type(test_fn2) == np.ndarray,\
            "Output2 is the wrong type"

    def test_IntensityMap(self):
        assert os.stat(test_vid).st_size > 0,\
            "File is empty"
        test_img_name = 'test'
        test_img_path = '.'
        scale_percent = 1
        test_thresh1 = 5
        test_thresh2 = 50000
        test_fn1 = GenerateIntensityMap.IntensityMap(test_vid, test_thresh1,
                                                     scale_percent,
                                                     test_img_path,
                                                     test_img_name)
        test_fn2 = GenerateIntensityMap.IntensityMap(test_vid, test_thresh2,
                                                     scale_percent,
                                                     test_img_path,
                                                     test_img_name)
        # Testing output type
        assert type(test_fn1) == matplotlib.collections.QuadMesh,\
            "Output1 is the wrong type"
        assert type(test_fn2) == matplotlib.collections.QuadMesh,\
            "Output2 is the wrong type"
