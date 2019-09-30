from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
   name='pipenv2setup',
   version='0.1.2',
   description='Library to generate install_requires.py file from pipfile',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='Alan Bacon',
   author_email='alan@bacontowers.co.uk',
   packages=['pipenv2setup'],
   install_requires=[
      'tomlkit'
   ],
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License"
   ],
   url='https://github.com/alanbacon/pipenv2setup'
)