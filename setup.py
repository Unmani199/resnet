
from setuptools import setup, find_packages

setup(
    name='resnet',
    version='0.1.0',
    description='Measuring graph resilience or network robustness',
    author='Unmani J',
    author_email='unmani.jaygude@ucdconnect.ie',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['plotly', 'networkx', 'scipy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.11.5'
)
