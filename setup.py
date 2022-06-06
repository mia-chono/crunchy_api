import os

import setuptools


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="crunchy_api",
    version="0.0.1",
    author="Mia Chono",
    description=("A Python API for Crunchyroll (beta)."),
    license="MIT",
    url="https://github.com/mia-chono/crunchy_api",
    install_requires=[
        "requests",
    ],
    long_description=read('README'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
)
