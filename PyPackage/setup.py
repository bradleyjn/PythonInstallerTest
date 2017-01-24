from distutils.core import setup

setup(
    name='PyPackage',
    version='1.0',
    author='Bradley Natarian',
    description='A test python package',
    packages=['PyPackage'],
    install_requires=['pandas'],
)