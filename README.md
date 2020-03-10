[![Build Status](https://travis-ci.com/cmcalli716/flashing_lights.svg?branch=master)](https://travis-ci.com/cmcalli716/flashing_lights)
# Flashing Lights
## Image Stack Processing Software for Fluorescence Microscopy in Research
This software package can be utilized in fluorescence imaging analysis to
effectively communicate information present within video files.
Functions present within the program are
designed to:

* Identify Regions of Interest (R.O.I.) based on relative pixel brightness
* Track ROI throughout the image stack and provide individual fluorescence intensity vs. time profiles
* Accumulate ROI counts throughout the stack and return a frequency heat map
* Accumulate ROI intensity throughout the stack and return an intensity heat map

### Cloning the flashing_lights repository
* Through cloning this repository, users will get the full functionality of
flashing_lights, as well as:
    * full documentation
    * examples of the code being executed
    * a virtual environment preloaded with python packages needed to run the code

#### Activating the virtual environment
* Included within the root of the repository is a virtual environment
pre-suited to run `flashing_lights`
  * The virtual environment is located within the root of the repository
  * To activate the virtual environment, after cloning,
  enter into the command prompt:
`source activate ~/<path to>/flashing_lights/flashing_lights_venv`
  * The environment contains:
    * Python 3.7 from miniconda3
    * numpy
    * os
    * pandas
    * cv2
    * matplotlib


### Installing flashing_lights through the command line
***Include install information here***
`conda install flashing_lights`

### Using flashing_lights
* Once installed, flashing_lights can be executed through a jupyter notebook.
  * It is recommended to run the code within the flashing_lights_venv
  virtual environment to avoid dependency hell
  * We have included a filled example of a jupyter notebook
  within `flashing_lights/examples` that demonstrates how to use the code.
  To access this notebook, enter the following into the command line:
  `jupyter notebook ~/<path to>/flashing_lights/examples/fl_example_nb.ipynb`
***Include an example jupyter notebook***
  * There is an empty notebook within the root of the repository that can serve
  as a template for users who are new to Python but would like to use this
  software package. To access this notebook, enter the following
  into the command line:
  `jupyter notebook ~/<path to>/flashing_lights/flashing_lights/fl_nb_template.ipynb`

### Miscellaneous Notes
  * In regards to PEP8 compliance of the frequency_1.py file, pylint shoots back an error I1101. 
  The '.pylintrc' file can be downloaded to prevent those from showing up in the terminal. 

### Preview of the results

***Include screenshots of us using the code***
