from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "r") as requirements_file:
    requirements = [line.rstrip() for line in requirements_file]

setup(
    name="yahoo",
    version="0.1.0",
    author="Bernardo Paulsen",
    author_email="bernardopaulsen@gmail.com",
    description="A package to import data from Yahoo Finance! API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/bernardopaulsen/yahoo",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        ],
)
