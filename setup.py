# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

# Get version from __version__ in spine/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('spine/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='spine',
    version=version,
    description='Spine Adapter',
    author='ElasticRun',
    author_email='engineering@elastic.run',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
)
