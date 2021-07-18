from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
	name='randomstuff.py',
	version='1.6.1',
	description='An easy to use & feature-rich python API wrapper for Random Stuff API.',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/nerdguyahmad/randomstuff.py',
	author='nerdguyahmad',
	author_email='nerdguyahmad.contact@gmail.com',
	license='MIT',
	classifiers=[
	'Development Status :: 3 - Alpha',
	'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',

	],
	keywords='api-wrapper randomstuff api wrapper',
	project_urls={
    'Documentation': 'https://nerdguyahmad.gitbook.io/randomstuff',
    'Source': 'https://github.com/nerdguyahmad/randomstuff.py',
    'Tracker': 'https://github.com/nerdguyahmad/randomstuff.py/issues',
	},
	install_requires=['aiohttp', 'requests', 'colorama'],
	python_requires='>=3.6',
	packages=find_packages(include=['randomstuff', 'randomstuff.*']),
	)
