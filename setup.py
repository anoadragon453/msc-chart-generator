#!/usr/bin/env python3
from setuptools import find_packages, setup


setup(
    name="msc-chart-generator",
    version="0.0.1",
    url="https://github.com/anoadragon453/msc-chart-generator",
    description="A library to generate MSC charts",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "plotly>=4.7.1",
        "pandas>=1.0.3",
        "psutil>=5.7.0",
        "progress>=1.5",
    ],
    extras_require={
        "dev": [
            "isort==5.0.4",
            "flake8==3.8.3",
            "flake8-comprehensions==3.2.3",
            "black==19.10b0",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
