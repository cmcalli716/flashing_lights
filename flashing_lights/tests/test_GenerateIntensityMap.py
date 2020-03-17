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
        assert os.stat(test_vid).stat().st_size > 0,\
            "File is empty"
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
        test_fn = GenerateIntensityMap.GetIntensityValues(test_img_resized,
                                                          test_thresh)
        # Testing output size
        assert len(test_fn) == len(test_img_resized),\
            "Output is the wrong shape"
        # Testing output type
        assert type(test_fn) == np.ndarray,\
            "Output is the wrong type"

    def test_GetIntensityArray(self):
        test_ret, test_img = cv2.imreadmulti(test_vid,
                                             flags=cv2.IMREAD_GRAYSCALE)
        # Setting Resizing Dimensions
        scale_percent = 1
        width = int(test_img[0].shape[1] * scale_percent / 100)
        height = int(test_img[0].shape[0] * scale_percent / 100)
        dim = (width, height)
        # Checking for valid dimensions
        self.assertIn(0, dim, msg="Invalid Dimensions")
        test_img_resized = cv2.resize(test_img[0], dim,
                                      interpolation=cv2.INTER_AREA)
        test_thresh = 5
        test_fn = GenerateIntensityMap.GetIntensityArray(test_vid, test_thresh,
                                                         scale_percent)
        # Testing output size
        assert len(test_fn) == len(test_img_resized),\
            "Output is the wrong shape"
        # Testing output type
        assert type(test_fn) == np.ndarray,\
            "Output is the wrong type"

    def test_IntensityMap(self):
        test_img_name = 'test'
        test_img_path = '.'
        scale_percent = 1
        test_thresh = 5
        num_figures_before = matplotlib.pyplot.gcf().number
        test_fn = GenerateIntensityMap.IntensityMap(test_vid, test_thresh,
                                                    scale_percent,
                                                    test_img_path,
                                                    test_img_name)
        num_figures_after = matplotlib.pyplot.gcf().number
        assert num_figures_before < num_figures_after,\
            "Plotting went astray"
        # Testing output type
        assert type(test_fn) == matplotlib.collections.QuadMesh,\
            "Output is the wrong type"
