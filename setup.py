#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', "numpy==1.26.4", "matplotlib==3.8.3", "PyYAML==6.0.1", "pydantic==2.6.4", "scipy==1.12.0"]

test_requirements = [ ]

setup(
    author="Harold",
    author_email='haroldjin@xdevbase.com',
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
    description="Graphing Calculator for the course",
    entry_points={
        'console_scripts': [
            'gies_imba_fin574_graphing_calculator=gies_imba_fin574_graphing_calculator.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gies_imba_fin574_graphing_calculator',
    name='gies_imba_fin574_graphing_calculator',
    packages=find_packages(include=['gies_imba_fin574_graphing_calculator', 'gies_imba_fin574_graphing_calculator.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/XD/gies_imba_fin574_graphing_calculator',
    version='0.1.0',
    zip_safe=False,
)
