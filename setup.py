from setuptools import setup

setup(
	name = 'CalenderDiffPlanner',
	version = '0.1.2',
	packages = ['CalenderDiffPlanner','res'],
	entry_points = {
		'console_scripts': [
		'CalenderDiffPlanner = CalenderDiffPlanner.__main__:main']
	})