from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
    readme = readme_file.read()
    requirements = [
        "datetime>=4.3",
        "numpy>=1.21.1",
        "pandas>=1.3.0",
        "pandas-datareader>=0.10.0"
        ]
    setup(
        name="yahoo",
        version="0.1.3",
        author_email="bernardopaulsen@gmail.com",
        author="Bernardo Paulsen",
        description="A package to import data from Yahoo Finance! API.",
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://yahoo.readthedocs.io/en/latest/",
        packages=find_packages(),
        install_requires=requirements,
        classifiers=[
            "Programming Language :: Python :: 3.9",
            "License :: OSI Approved :: MIT License",
            ],
        )
