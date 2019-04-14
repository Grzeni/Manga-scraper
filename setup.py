from setuptools import setup

setup(name='manga_scraper',
	version='1.0',
	description='mangareader.net manga scans scraper',
	author='Grzegorz Winiarski',
	author_email='288337@uwr.edu.pl',
	packages=['manga_scraper'],
	install_requires=[
	'requests',
	'bs4']
	)