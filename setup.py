from distutils.core import setup

setup(
    name='PyPackage',
    version='1.0',
    author='Bradley Natarian',
    description='A test python package',
	package_data={'PyPackage.Resources': [*.csv],
							  'PyPackage.Resources2':[*]},
    packages=['PyPackage'],
    install_requires=['pandas'],
)