import os
import numpy as np
from setuptools import setup, find_packages, Extension


NAME = 'toad'


CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))
VERSION_FILE = os.path.join(CURRENT_PATH, NAME, 'version.py')

def get_version():
    ns = {}
    with open(VERSION_FILE) as f:
        exec(f.read(), ns)
    return ns['__version__']


def get_ext_modules():
    from Cython.Build import cythonize

    extensions = [
        Extension('toad.c_utils', sources = ['toad/c_utils.pyx'], include_dirs = [np.get_include()]),
        Extension('toad.merge', sources = ['toad/merge.pyx'], include_dirs = [np.get_include()]),
    ]

    return cythonize(extensions)


def get_requirements(stage = None):
    file_name = 'requirements'

    if stage is not None:
        file_name = f"{file_name}-{stage}"
    
    requirements = []
    with open(f"{file_name}.txt", 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('-'):
                continue
            
            requirements.append(line)
    
    return requirements


setup(
    include_dirs = [np.get_include()],
    ext_modules = get_ext_modules(),
    include_package_data = True,
    python_requires = '>=3.8',
    setup_requires = ['numpy'],
    tests_require = get_requirements('test'),
    entry_points = {
        'console_scripts': [
            'toad = toad.cli:main',
        ],
    },
)
