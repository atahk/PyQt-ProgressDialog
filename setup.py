#!/usr/bin/env python
# --*-- coding: utf-8 --*--

from distutils.core import setup

setup(
    name="PyQt-ProgressDialog",
    version="0.1.1",
    description="PyQt Progress Dialog",
    author="Jack Lam",
    author_email="jacklam718@gmail.com",
    url="https://github.com/atahk/PyQt-ProgressBar",
    install_requires=[
        'PyQt5',
    ],
    py_modules=["QtProgressDialog"],
)
