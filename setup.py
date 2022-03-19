from setuptools import setup, find_packages
import os

setup(
    name='docker-images',
    version='0.1.0',
    description='Imagens Docker',
    url='git@github.com:upgrade-php/docker-images.git',
    author='Vicente Pinheiro',
    author_email='vpp.filho@gmail.com',
    license='unlicense',
    zip_safe=False,
    package_dir={"faprod": "faprod"},
)