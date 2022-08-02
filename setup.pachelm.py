#!/usr/bin/env python
import codecs
import os.path
import re
import sys

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

install_requires = [
    # 'botocore==1.27.42',
    # 'docutils>=0.10,<0.17',
    # 's3transfer>=0.6.0,<0.7.0',
    # 'PyYAML>=3.10,<5.5',
    # 'colorama>=0.2.5,<0.4.5',
    # 'rsa>=3.1.2,<4.8',
]

setup(
     name='qtft-sor-logistics-cli',  
     version=find_version("sor", "__init__.py"),
     scripts=['bin/sor'] ,
     author="Krittin Phornsiricharoenphant",
     author_email="krittin@qtft.org",
     description="QTFT SOR Logistics SaaS API wrapper as Command line cli and Python SDK",
     long_description=read('README.rst'),
     long_description_content_type="text/markdown",
     url="https://github.com/sinonkt/sor-logistic-cli",
     packages=find_packages(exclude=['tests*']),
    #  package_data={'xxxx': ['xxxx/templates/*.tmpl']},
     install_requires=install_requires,
     python_requires=">= 3.10",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD-2-Clause license",
         "Operating System :: OS Independent",
     ],
     project_urls={
        'Source': 'https://github.com/aws/aws-cli',
        'Reference': 'https://docs.aws.amazon.com/cli/latest/reference/',
        'Changelog': 'https://github.com/aws/aws-cli/blob/develop/CHANGELOG.rst',
    },
 )