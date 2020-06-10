from setuptools import setup, find_packages
from os import path


def get_readme():
    here = path.dirname(__file__)
    with open(path.join(here, 'README.md'), encoding='UTF8') as readme_file:
        readme = readme_file.read()
        return readme

setup(
    name="pyplayscii",
    version="0.0.1",
    author="SeBeom Lee",
    description="Unity style ascii art game engine",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/k2sebeom/pyplayscii",
    packages=find_packages(include=['playscii']),
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)