from distutils.core import setup

setup(
    name='PyPackage',
    version='1.0',
    author='Bradley Natarian',
    description='A test python package',
	packages=['PyPackage'],
	package_data={'PyPackage.Resources': ['*.csv'],
							  'PyPackage.Resources2':['*']},
    install_requires=['pandas'],
)