from setuptools import setup

setup(
	name = 'diff-planner',
	version = '0.1.2',
	packages = ['src','res'],
	entry_points = {
		'console_scripts': [
		'diff-planner = src.__main__:main']
	})