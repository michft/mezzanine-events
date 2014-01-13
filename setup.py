import codecs
from setuptools import setup, find_packages
from mezzanine_events import __version__
import subprocess

#def get_long_desc():
#	"""Use Pandoc to convert the readme to ReST for the PyPI."""
#	try:
#		return subprocess.check_output(['pandoc', '-f', 'markdown', '-t', 'rst', 'README.mdown'])
#	except:
#		print "WARNING: The long readme wasn't converted properly"
### manually worked around bad pandoc call (problem with unicode)

setup(name='mezzanine-events',
	version=__version__,
	description='Event pages for the Mezzanine CMS',
	long_description=codecs.open('README.rst', encoding='utf-8').read(),
	author='Adam Brenecki',
	author_email='abrenecki@sbtc.org.au',
	url='https://github.com/stbarnabas/mezzanine-events',
	packages=find_packages(),
	include_package_data=True,
	setup_requires=[
		'setuptools_git>=0.3',
	],
	install_requires=[
	    'mezzanine',
		'icalendar==3.0.1b2',
		'geopy==0.95.1',
		'pytz',
	],
	classifiers = [
		'Development Status :: 4 - Beta',
		'Environment :: Web Environment',
		'Framework :: Django',
		'License :: OSI Approved :: MIT License',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
	],
)
