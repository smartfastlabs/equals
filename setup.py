from distutils.core import setup

import equals

with open('README.rst') as f:
    long_description = f.read()

setup(
    description='Python Fuzzy Matchers',
    long_description=long_description,
    name='equals',
    version=equals.__version__,
    author='Todd Siflet',
    author_email='todd.siflet@gmail.com',
    py_modules = [],
)
