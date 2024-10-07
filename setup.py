import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="N1081B-SDK",
    version="1.0.0",
    author="Nuclear Instruments",
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["websocket"],
)
