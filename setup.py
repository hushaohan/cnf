#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'click',
    # TODO: put package requirements here
]

setup(
    name='cnf',
    version='0.1.0',
    description="CNF Tools",
    long_description=readme + '\n',
    author="Shaohan Hu",
    author_email='shaohan.hu@ibm.com',
    url='https://github.ibm.com/Shaohan-Hu/cnf',
    packages=find_packages(include=['cnf']),
    entry_points={
        'console_scripts': [
            'cnf=cnf.cli:entry_point'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='cnf',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
