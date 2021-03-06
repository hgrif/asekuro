import asekuro
from setuptools import setup, find_packages
from os import path


def load_readme():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(
    name='asekuro',
    version=asekuro.__version__,
    description='CLI util to deal with Jupyter Notebooks',
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    license='MIT License',
    author='Vincent D. Warmerdam',
    entry_points={
        'console_scripts': [
            'asekuro = asekuro.commandline:main',
        ],
    },
    url='https://github.com/godatadriven/asekuro',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['pytest==3.7.0',
                      'nbval==0.9.1',
                      'fire==0.1.3',
                      'nbformat==4.4.0',
                      'ipython==6.5.0',
                      'jupyter-client==5.2.3',
                      'jupyter-core==4.4.0'],
    classifiers=['Topic :: Software Development :: Build Tools',
                 'Topic :: Utilities',
                 'Framework :: Jupyter',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'Programming Language :: Python :: 3.6',
                 'Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License']
)
