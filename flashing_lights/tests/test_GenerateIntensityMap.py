import numpy as np
import cv2
import os
from flashing_lights import GenerateIntensityMap
import requests
import unittest


class test_GenerateIntensityMap(unittest.TestCase):

    def test_GetIntensityValues():
        # Download video from repo for testing
        filename = 'test.tif'
        url = 'https://github.com/cmcalli716/flashing_lights/\
        blob/master/flashing_lights/data/July_test.tif?raw=true'
        req = requests.get(url)
        assert req.status_code == 200,\
            "Download failed"
        with open(filename, 'wb') as f:
            f.write(req.content)
        test_ret, test_img = cv2.imreadmulti('test.tif',
                                             flags=cv2.IMREAD_GRAYSCALE)
        test_thresh = 5
        test_fn = GenerateIntensityMap.GetIntensityValues(test_img[0],
                                                          test_thresh)
        # Testing output size
        assert len(test_fn) == len(test_img[0]),\
            "Output is the wrong shape"
        # Testing output type
        assert type(test_fn) == np.ndarray,\
            "Output is the wrong type"
        assert np.mean(test_fn) > 0,\
            "No counts were found in test image"

    def test_GetIntensityArray():
        # Download video from repo for testing
        filename = 'test.tif'
        url = 'https://github.com/cmcalli716/flashing_lights/\
        blob/master/flashing_lights/data/July_test.tif?raw=true'
        req = requests.get(url)
        assert req.status_code == 200,\
            "Download failed"
        with open(filename, 'wb') as f:
            f.write(req.content)
        test_ret, test_img = cv2.imreadmulti('test.tif',
                                             flags=cv2.IMREAD_GRAYSCALE)
        test_thresh = 5
        scale = 1
        test_fn = GenerateIntensityMap.GetIntensityArray('test.tif',
                                                         test_thresh, scale)
        # Testing output size
        assert len(test_fn) == len(test_img[0]),\
            "Output is the wrong shape"
        # Testing output type
        assert type(test_fn) == np.ndarray,\
            "Output is the wrong type"
        assert np.mean(test_fn) > 0,\
            "No counts were found in test video"

    def test_IntensityMap():
        test_img_name = 'test'
        test_img_path = '/mnt/c/Users/'
        # Download video from repo for testing
        filename = 'test.tif'
        url = 'https://github.com/cmcalli716/flashing_lights/\
        blob/master/flashing_lights/data/July_test.tif?raw=true'
        req = requests.get(url)
        assert req.status_code == 200,\
            "Download failed"
        with open(filename, 'wb') as f:
            f.write(req.content)
        test_ret, test_img = cv2.imreadmulti('test.tif',
                                             flags=cv2.IMREAD_GRAYSCALE)
        test_thresh = 5
        scale = 1
        test_fn = GenerateIntensityMap.IntensityMap('test.tif', test_thresh,
                                                    scale, test_img_path,
                                                    test_img_name)
        # Checking to see if array used for plotting is multidimensional
        assert test_fn.ndim > 0,\
            "Wrong dimensional array used for plotting"
        # Checking to see if file is empty or not
        assert os.path.getsize(test_img_path + '/' + test_img_name) > 0,\
            "Saved file is empty."
