from setuptools import setup
from typing import List

#Declaring variables for setup function

NAME = "Housing-Predictor"
VERSION = "0.0.1"
AUTHOR = "SHALAKA VAZE"
DESCRIPTION="This is a houseing price prediction app which will predict the prices of the houses on given attributes"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Desription: This function will read the reured modules/packages mentioned 
    in the requirements.txt file and return those names as the list"""

    with open(REQUIREMENT_FILE_NAME) as requirement:
        return requirement.readlines()


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()

)

""" if __name__=="__main__":
    print(get_requirements_list()) """