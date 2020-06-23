from setuptools import setup, find_packages
from os import path


def get_readme():
    here = path.dirname(__file__)
    with open(path.join(here, 'README.md'), encoding='UTF8') as readme_file:
        readme = readme_file.read()
        return readme


def get_requirements():
    here = path.dirname(__file__)
    with open(path.join(here, 'requirements.txt'), encoding='UTF8') as req_file:
        req = req_file.read()
        return req


setup(
    name="pyplayscii",
    version="0.1.3",
    author="SeBeom Lee",
    description="Object oriented ascii art python game engine",
    long_description=get_readme(),
    install_requires=get_requirements(),
    long_description_content_type="text/markdown",
    url="https://github.com/k2sebeom/pyplayscii",
    packages=find_packages(include=['playscii', 'playscii.games']),
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
