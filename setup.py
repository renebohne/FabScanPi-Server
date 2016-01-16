__author__ = 'mariolukas'
from distutils.core import setup
from setuptools import find_packages
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), "src"))

DEPENDENCY_LINKS = []
INSTALL_REQUIRES = []
EXTRA_REQUIRES = dict()

def package_data_dirs(source, sub_folders):
	import os
	dirs = []

	for d in sub_folders:
		folder = os.path.join(source, d)
		if not os.path.exists(folder):
			continue

		for dirname, _, files in os.walk(folder):
			dirname = os.path.relpath(dirname, source)
			for f in files:
				dirs.append(os.path.join(dirname, f))

	return dirs



def params():
    version = "0.1.4r1"
    name = "FabScanPi"
    description = "FabScanPi is a Stand-alone Web-enabled Open-Source 3D Laser Scanner Software"
    long_description = open("README.md").read()
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: JavaScript",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Printing",
        "Topic :: System :: Networking :: Monitoring"
    ]
    author = "Mario Lukas"
    author_email = "mario@fabscan.org"
    url = "http://www.fabscan.org"
    license = "AGPLv3"


    packages = find_packages(where="src")
    package_dir = {
        "": "src"
    }


    include_package_data = True
    zip_safe = False
    install_requires = INSTALL_REQUIRES
    extras_require = EXTRA_REQUIRES
    dependency_links = DEPENDENCY_LINKS

    if os.environ.get('READTHEDOCS', None) == 'True':
        # we can't tell read the docs to please perform a pip install -e .[develop], so we help
        # it a bit here by explicitly adding the development dependencies, which include our
        # documentation dependencies
        install_requires = install_requires + extras_require['develop']


    data_files = [
        ('/etc/fabscanpi/', ['src/fabscan/config/default.settings.json']),
        ('/etc/fabscanpi/', ['src/fabscan/config/default.config.json']),
        ('/usr/local/fabscanpi/www/', ['src/www/index.html']),
        ('/usr/local/fabscanpi/www/style/',['src/www/style/app.css', 'src/www/style/lib.css']),
        ('/usr/local/fabscanpi/www/js/',['src/www/js/app.js', 'src/www/js/lib.js']),
        ('/usr/local/fabscanpi/www/icons/', ['src/www/icons/favicon.png'])
    ]

    scripts=['src/fabscanpi-server']


    return locals()

setup(**params())
