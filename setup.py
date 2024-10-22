from setuptools import setup

setup(
    name='resnet',
    version='0.0.1',    
    description='Python package to measure network resilience',
    url='https://github.com/Unmani199/resnet.git',
    author='Unmani J',
    author_email='unmani.jaygude@ucdconnect.ie',
    license='None',
    packages=['resnet'],
    python_requires=">=3.6",
    install_requires=['pandas>=2.0.3','plotly>=5.9.0','networkx>=3.1'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: None :: None',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
