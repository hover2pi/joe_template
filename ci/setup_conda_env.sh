#!/bin/bash

echo "Creating a Python $PYTHON_VERSION environment"
conda create -n my_env python=$PYTHON_VERSION || exit 1
source activate my_env

echo "Installing packages..."
conda install flake8 beautifulsoup4 lxml numpy astropy
pip install pytest pytest-cov coveralls
