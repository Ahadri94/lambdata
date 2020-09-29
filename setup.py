# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-19", # the name that you will install via pip
    version="3.8",
    author="Ahmed Hadri",
    author_email="hadri-ahmed@lambdastudents.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/Ahadri94/lambdata-hadri",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)