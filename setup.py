from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."

## Function to gather all the required packages
def get_requirements(filename):
    """
    Return all the requirements from the given filename
    """

    requirements = []

    with open(filename) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
name = 'ML_Project1',
version='0.0.1',
author="Krishnakanth",
author_email="jkkn.iitkgp@outlook.com",
packages=find_packages(),
install_requires = get_requirements("requirements.txt")

)