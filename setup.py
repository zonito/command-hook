"""Setup file for pre-commit."""

from setuptools import find_packages
from setuptools import setup

setup(
    name='command-hooks',
    description='Run command before commit.',
    url='https://github.com/zonito/command-hook.git',
    version='0.0.1',
    author='Love Sharma',
    author_email='contact@lovesharma.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages('.'),
    entry_points={
        'console_scripts': [
            'cmd=command_hook.command:main'
        ],
    },
)
