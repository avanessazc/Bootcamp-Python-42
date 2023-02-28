#!/usr/bin/env bash

## Usage:
# python -m venv tmp_env && source tmp_env/bin/activate
# bash ./build.sh

### Use latest versions of setuptools and wheel installed:
python -m pip install --upgrade pip setuptools wheel

# https://realpython.com/python-wheels/#:~:text=A%20universal%20wheel%20is%20a,%5Bbdist_wheel%5D%20universal%20%3D%201
python setup.py sdist bdist_wheel

pip install ./dist/my_minipack-1.0.0.tar.gz
# pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
