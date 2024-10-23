from setuptools import setup, Command
import os

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
        'Intended Audience :: Science/Research',
        'Operating System :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)


class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

# Further down when you call setup()
setup(
    # ... Other setup options
    cmdclass={
        'clean': CleanCommand,
    }
)
