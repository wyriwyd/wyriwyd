#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['mistletoe', 'pygments']
repositories = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'flake8', 'pytest-cov']

setup(
    author="SSI hackers",
    author_email='a.j.jackson@physics.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="",
    entry_points={
        'console_scripts': [
            'wyriwyd-test=wyriwyd.__main__:main',
        ],
    },
    install_requires=requirements,
    dependency_links=repositories,
    license="BSD 3-clause",
    long_description=readme,  # + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=['documentation', 'testing'],
    name='wyriwyd',
    packages=find_packages(include=['wyriwyd']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='http://github.com/wyriwyd/wyriwyd',
    version='0.1.0',
    zip_safe=True,
)
