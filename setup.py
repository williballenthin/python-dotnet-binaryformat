#!/usr/bin/env python

import setuptools


description = "Pure Python parser for .NET BinaryFormatter serialized data."
setuptools.setup(name="python-dotnet-binaryformat",
                 version="0.1",
                 description=description,
                 long_description=description,
                 author="Willi Ballenthin",
                 author_email="william.ballenthin@fireeye.com",
                 url="https://github.com/williballenthin/python-dotnet-binaryformat",
                 license="Apache 2.0 License",
                 install_requires=[
                     "pytest",
                     "hexdump",
                     "vivisect-vstruct-wb",
                 ],
                 packages=setuptools.find_packages())
