#!/usr/bin/env python3

from setuptools import setup, find_packages

install_requires = [
    'requests>=2.13.0',
]
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='zebulon',
    version='1.0.0',
    author='Marc Arbesman',
    author_email='marbesman@gmail.com',
    url='https://github.com/willcode4food/zebulon',
    packages=find_packages(),
    install_requires=install_requires,
    # tests_require=tests_require,
    # extras_require={
    #     'test': tests_require,
    # },
    description='A theory on crypto trading',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # download_url='https://github.com/danpaquin/coinbasepro-python/archive/master.zip',


)
