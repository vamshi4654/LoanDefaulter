from setuptools import find_packages,setup
from typing import List

HYPEN_DOT = "-e ."
def get_requriements(filepath:str)-> list[str]:
    '''
    this function will give the requirements in a list
    '''
    requirements = []
    with open(filepath) as file_object:
        requirements = file_object.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)

    return requirements


setup(
name = "LoanDefaultor",
version = 0.1,
description = "building the packages for loan defaultes",
author= 'vamshi',
author_email= "g.vamshi123@gmail.com",
packages= find_packages(),
install_requires = get_requriements("requirements.txt")
)