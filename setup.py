from setuptools import setup, find_packages
import sys, os

version = 'mkdir ckanext-MYEXTENSION-CUSTOMFIELDS\rcd ckanext-MYEXTENSION-CUSTOMFIELDS1'

setup(
	name='ckanext-MYEXTENSION',
	version=version,
	description="2",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='3',
	author_email='4',
	url='5',
	license='6',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.usmetadata'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	# myplugin=ckanext.MYEXTENSION:PluginClass
	usmetadata=ckanext.usmetadata.plugin:USMetadataPlugin
	""",
)
