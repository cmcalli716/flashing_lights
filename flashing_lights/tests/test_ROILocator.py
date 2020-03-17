import os
import unittest

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import skimage
import skimage.io as sio
from skimage.feature import blob_dog
import cv2

import flashing_lights
from flashing_lights import ROILocator as RL


file_name = 'test_ROI.tif'
data_path = os.path.join(flashing_lights.__path__[0], 'data')
test_vid = os.path.join(data_path, file_name)

gray_name = 'test_gray.tif'
gray_test_vid = os.path.join(data_path, gray_name)

class test_ROILocator(unittest.TestCase):
    
    def test_gray_scaler(self):
        # Test output data type.
        assert RL.gray_scaler(test_vid).dtype == 'uint16',\
            "Wrong output data type."
        
        
    def test_img_normalizer(self):
        test_img = sio.imread(gray_test_vid)
        test_norm, test_mean, test_std = RL.img_normalizer(test_img)
        # Test output value range.
        assert test_norm.min() == 0.,\
            "Wrong minimun value."
        assert test_norm.max() == 255.,\
            "Wrong maximun value."
        
    
    def test_diff_of_gauss(self):
        test_img, test_mean, test_std = RL.img_normalizer(sio.imread(gray_test_vid))
        test_a = 1
        test_b = 3
        test_c = 0.1
        test_roi = RL.diff_of_gauss(test_img, test_mean, test_std, test_a, test_b, test_c)
        # Test output dimensions.
        assert len(test_roi[0][0]) == 3,\
            "Wrong output dimensions."
        
   
    def test_ROI_counting(self):
        test_img, test_mean, test_std = RL.img_normalizer(sio.imread(gray_test_vid))
        test_a = 1
        test_b = 3
        test_c = 0.1
        test_roi = RL.diff_of_gauss(test_img, test_mean, test_std, test_a, test_b, test_c)
        test_length = len(test_img) - 1
        test_roi_number = RL.ROI_counting(test_roi, test_length)
        # Test output value sign.
        assert test_roi_number >= 0,\
            "Output should always be positive."
        
        
    def test_ROI_counting_list(self):
        test_img, test_mean, test_std = RL.img_normalizer(sio.imread(gray_test_vid))
        test_a = 1
        test_b = 3
        test_c = 0.1
        test_roi = RL.diff_of_gauss(test_img, test_mean, test_std, test_a, test_b, test_c)
        test_list = RL.ROI_counting_list(test_img, test_roi)
        # Test output property.
        assert isinstance(test_list, list),\
            "Output should always be a list."
       
    
    def test_plot_and_save(self):
        test_img, test_mean, test_std = RL.img_normalizer(sio.imread(gray_test_vid))
        test_a = 1
        test_b = 3
        test_c = 0.1
        test_roi = RL.diff_of_gauss(test_img, test_mean, test_std, test_a, test_b, test_c)
        test_list = RL.ROI_counting_list(test_img, test_roi)
        path_list = RL.plot_and_save(test_img, data_path, test_roi, test_list)
        # Test output property.
        assert isinstance(path_list, list),\
            "Output should always be a list."
        
        
    def test_video_writer(self):
        test_img, test_mean, test_std = RL.img_normalizer(sio.imread(gray_test_vid))
        test_a = 1
        test_b = 3
        test_c = 0.1
        test_roi = RL.diff_of_gauss(test_img, test_mean, test_std, test_a, test_b, test_c)
        test_list = RL.ROI_counting_list(test_img, test_roi)
        path_list = RL.plot_and_save(test_img, data_path, test_roi, test_list)
        video_path = RL.video_writer(path_list, data_path)
        # Test output path existence.
        assert os.path.isfile(video_path),\
            "Video not existing due to output error."
        
        
    def test_ROI_locator(self):
        test_mean = 1
        test_std = 3
        test_overlap = 0.1
        video_path = RL.ROI_locator(test_vid, data_path, test_mean, test_std, test_overlap)
        # Test output path existence.
        assert os.path.isfile(video_path),\
            "Video not existing due to output error."