import setuptools


with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="string_matching",
    version="0.0.1",
    author="Bogdan Kostić",
    description="A commandline tool for searching strings in text.",
    long_description=long_description,
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)
