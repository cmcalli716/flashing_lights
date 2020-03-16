[![Build Status](https://travis-ci.com/cmcalli716/flashing_lights.svg?branch=master)](https://travis-ci.com/cmcalli716/flashing_lights)
[![Coverage Status](https://coveralls.io/repos/github/cmcalli716/flashing_lights/badge.svg?branch=master)](https://coveralls.io/github/cmcalli716/flashing_lights?branch=master)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
# 
![Alt Text](lights.gif)
# Flashing Lights
## Image Stack Processing Software for Fluorescence Microscopy in Research
* This software package can be utilized in fluorescence imaging analysis to
effectively communicate information present within video files.
Functions present within the program are
designed to:

  * Identify Regions of Interest (R.O.I.) based on relative pixel brightness
  * Accumulate ROI counts throughout the stack and return a frequency heat map
  * Accumulate ROI intensity throughout the stack and return an intensity heat map

#### Repository Structure
```
  |- README.md
  |- flashing_lights/
      |- __init__.py
      |- GenerateHeatMap.py
      |- GenerateIntensitymap.py
      |- tests/
        |- __init__.py
        |- test_GenerateHeatMap.py
        |- test_GenerateIntensityMap.py
      |- data/
        |-July_test.tif
  |- doc/
      |- functionality.md
      |- usage_cases.md
      |- tech_review.pdf
  |- examples/
      |- worked/ (contains worked examples and example images)
      |- templates/ (contains empty examples for users to input their own data)
  |- setup.py
  |- .travis.yml
  |- environment.yml
  |- .pylintrc (for pylint conflict with opencv)
  |- .gitignore
  |- lights.gif (Star Trek Video)
  |- ROI_video_example.gif
  |- LICENSE

```
#### Installing flashing_lights through the command line
*Include install information here* `conda install flashing_lights`

#### Activating the virtual environment
* Included within the root of the repository is a virtual environment
pre-suited to run `flashing_lights`
  * The virtual environment is located within environment.yml
  * To create the virtual environment from the .yml file:
  `conda env create -f environment.yml`
  * To activate the virtual environment:
  `conda activate flashing_lights_env`
  * The environment contains:
    * Python 3.8 from miniconda3
    * numpy
    * os
    * pandas
    * matplotlib
    * skimage
    * cv2

### Using flashing_lights
* Before using, please download some sample data that you can test the package with (UW members only):
  * https://drive.google.com/open?id=1_QdBC2IoNTqGhwI5b9mVSK-13hiPy7nv (Belongs to Chris)
  * https://drive.google.com/open?id=1mJFNPfbdzfQ6NuFcVwRL8FVMmbw3L43K (Belongs to Chris)
  * https://drive.google.com/open?id=1ZkAAcj-qXpCypLGnU8HuU47QkjAKdvko (Belongs to July)
  * https://drive.google.com/open?id=12Noa3-JsaPup9Ao9WEqEOqzdbKAMogCA (Belongs to July)
* Once installed, flashing_lights can be executed through a jupyter notebook.
  * It is recommended to run the code within the included
  virtual environment to avoid dependency hell
  * We have included filled examples of  jupyter notebooks
  within `flashing_lights/examples/worked` that demonstrate how to use the code.
  To access this notebooks, enter the following into the command line:
  `jupyter notebook flashing_lights/examples/worked/<notebook name>`
  * There are empty notebooks within `flashing_lights/examples/templates` that can serve
  as a template for users who are new to Python but would like to use this
  software package. To access this notebook, enter the following
  into the command line:
  `jupyter notebook flashing_lights/examples/templates/fl_nb_template.ipynb`

### Example Code Output
![Alt Text](ROI_video_example.gif)

### Miscellaneous Notes
  * In regards to PEP8 compliance of the GenerateHeatMap.py file, pylint shoots back an error I1101.
  The '.pylintrc' file can be downloaded to prevent those from showing up in the terminal.

### Special Thanks
  * A big shout to Professor Dave Beck, Professor Ting Cao, Caityln Wolf, Jimin Qian, Ted Cohen,
  and Torin Stetina for all of their help as TAs in the development of this package.
