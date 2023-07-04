from setuptools import find_packages,setup
from typing import List

hyphen_e_dot= '-e .'


def get_requiremtnts(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)

    return requirements









setup(
    name='Attack Type Prediction in Network Systems',
    version= 'v1.1.1',
    author_name ='Tushar Deep',
    author_email='d.tushar@outlook.com',
    install_requires = get_requiremtnts('requirements.txt'),
    packages=find_packages()
)
