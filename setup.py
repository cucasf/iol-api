#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 
    'aiohttp==3.8.1',
    'pandas==1.3.4'
 ]

test_requirements = ['pytest>=3', ]

setup(
    author="Lucas Matias Dentesani",
    author_email='cucasf@outlook.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="IOL API wrapper",
    install_requires=requirements,  
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['iol_api', 'api', 'async', 'iol', 'invertir online'],
    name='iol_api',
    packages=find_packages(include=['iol_api', 'iol_api.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/cucasf/iol-api',
    version='0.1.1',
    zip_safe=False,
)
