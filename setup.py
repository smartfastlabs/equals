from setuptools import setup

import equals

with open('README.rst') as f:
    long_description = f.read()

setup(
    description='Python Fuzzy Matchers',
    long_description=long_description,
    name='equals',
    version=equals.__version__,
    author='Todd Sifleet',
    author_email='todd.siflet@gmail.com',
    packages=['equals', 'equals.constraints'],
    zip_safe=True,
    license='MIT',
    url='https://github.com/toddsifleet/equals',
)
