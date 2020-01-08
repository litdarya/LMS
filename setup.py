#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='lms',
    version='0.0',
    packages=find_packages(),
    url='https://github.com/litdarya/LMS',
    license='MIT',
    author='litdarya',
    author_email="litv.daria@gmail.com",
    description='',
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    install_requires=[
    ],
    tests_require=[
        "pytest-pylint",
    ],
)
