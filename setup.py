import os
from setuptools import setup, find_packages

from repostack import __version__

current_path = os.path.dirname(os.path.abspath(__file__))
requirement_file = os.path.join(current_path, 'requirements.txt')

with open(requirement_file, 'r') as f:
    requires = [x.strip() for x in f if x.strip()]

setup(
    name='repostack',
    version=__version__,
    description='Command line tool for repo',
    packages=find_packages(exclude=['tests', 'docs']),
    package_data={"repostack": ["templates/*.tpl"]},
    install_requires=requires,
    entry_points={
        'console_scripts': ['cfcli=repostack:cli'],
    },
    author='eddyzhou',
    author_email='zhouqian1103@gmail.com',
    url='https://github.com/eddyzhou/repostack',
)

