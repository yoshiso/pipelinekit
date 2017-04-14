#!/usr/bin/env python
# coding: utf-8
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from ppkit import __author__, __version__, __license__


setup(
    name='ppkit',
    version=__version__,
    description='Pipe functions',
    license=__license__,
    author=__author__,
    author_email='nya060@gmail.com',
    url='https://github.com/yoshiso/ppkit.git',
    keywords='',
    packages=find_packages(),
    install_requires=[],
    tests_require=[
        'nose',
    ],
    setup_requires=["flake8"]
)
