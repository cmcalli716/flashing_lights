import os
import sys
from setuptools import setup

# Get appropriate version and release info
ver_file = os.path.join('flashing_lights', 'version.py')

# Grabs description from the README file
with open(ver_file) as f:
    exec(f.read())

# Give setuptools a hit to complain if it's too old of a version
# 24.2.0 added the python_requires option
# Enables setuptools to install wheel on-the-fly
#SETUP_REQUIRES = ['setuptools >= 24.2.0']
#SETUP_REQUIRES += ['wheel'] if 'bdist_wheel' in sys.argv else []

setup(name = 'flashing lights',
      description = 'A package for analyzing stacks of fluoorescnce imaging',
      description_content_type = 'text/markdown',
      long_description = open('README.md', 'r').read(),
      long_description_content_type = 'text/markdown',
      url = 'https://github.com/cmcalli76/flashing_lights',
      authors = 'Chris McAllister, Derek Mar, July Zhou, Robin Lin',
      license = 'MIT',

if __name__ == '__main__':
    setup(**opts)
