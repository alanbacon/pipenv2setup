## Description

This module can be used to generate a `install_requires.py` file from a `Pipfile`. The array in this file can then be imported into your `setup.py` file and used as the `install_requires` arguments in the `setup` function.


## Install

	>>> pipenv install --dev pipenv2setup

## Run

	>>> pipenv run python -m pipenv2setup

## Use

Create a `setup.py` file that follows this format:

```
from setuptools import setup
from install_requires import install_requires


setup(
   name='package_name',
   version='0.1.0',
   description='Library to do my cool thing',
   author='Victoria Snellgrove',
   packages=['package_name'],
   install_requires=install_requires
)
```