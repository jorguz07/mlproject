#app set up and some meta data
#what we install is 'requirements.txt', which triggers the installation of all listed packages in there. We
#also added '-e .' to the list, which tells the system there's a 'setup.py' file that buils the app

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        #requirements.txt has '-e .', which we don't want in this list
        if HYPEN_E_DOT in requirements: 
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='me',
author_email='jorguzjma07@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)

#packages attribute: find_packages() will look for any folders in our directory with ___init__.py 
#and consider them a package
#install_requires attribute: we create a function get_requirements() that will look for our requirements.txt file
#and install the packages there