from setuptools import find_packages,setup
from typing import List
HYP="-e ."
def get_requirements(filepath:str)->List[str]:
    requirements=[]
    with open(filepath,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] 
        if HYP in requirements:
            requirements.remove(HYP)
    return requirements

    

setup(
    name="hotelReview",
    version="0.0.1",
    author="ashiknazar",
    author_email="datas293@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),



)
