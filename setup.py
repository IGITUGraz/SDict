from setuptools import setup

from sdict import __version__ as FULL_VERSION

"""
This file installs the sdict package.
For updating the version, update __version__ in sdict/__init__.py
"""

setup(
    name="sdict",
    version=FULL_VERSION,
    packages=['sdict'],
    author="Arjun Rao, Anand Subramoney",
    author_email="arjun@igi.tugraz.at, anand@igi.tugraz.at",
    description="This module provides a map with dot access",
    provides=['sdict'],
)
