from distutils.core import setup

setup(
    name='PyPackage',
    version='1.0',
    author='Bradley Natarian',
    description='A test python package',
	packages=['PyPackage'],
	include_package_data=True,
    install_requires=['pandas'],
)