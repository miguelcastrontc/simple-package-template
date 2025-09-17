from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_package_teste",
    version="0.0.1",
    author="Miguel_Castro",
    author_email="silva.miguelcastro7@gmail.com",
    description="First package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/miguelcastrontc/simple-package-template"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
