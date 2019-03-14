#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = [
    "blosc>=1.8",
    "Jinja2",
    "mock>=2.0",
    "msgpack",
    "networkx",
    "orderedset",
    "procrunner>=0.6",
    "pytest>=3.6",
    "scikit_learn[alldeps]",
    "scipy",
    "six",
    "tqdm==4.23.4",
]
setup_requirements = []

setup(
    author="DIALS",
    author_email="dials-support@lists.sourceforge.net",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
    description="DIALS Dependencies",
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    long_description_content_type="text/x-rst",
    name="dials_dependencies",
    packages=find_packages(),
    setup_requires=setup_requirements,
    url="https://github.com/dials/dials-dependencies",
    version="0.1.0",
    zip_safe=False,
)