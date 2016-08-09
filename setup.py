from distutils.core import setup
from setuptools import find_packages
import codecs

def long_description():
    with codecs.open('README.rst', 'r') as f:
        return f.read()

setup(
    name = 'sakshat',
    packages = find_packages(exclude = ['saks-v1.x', 'examples', 'docs']),
    version = '0.0.2',
    description = 'A fully packaged SAKS SDK',
    long_description = long_description(),
    author = 'Spoony',
    author_email = 'me@wangxianyuan.com',
    url = 'https://github.com/spoonysonny/SAKS-SDK',
    download_url = 'https://github.com/spoonysonny/SAKS-SDK/tarball/master',
    keywords = ['sdk', 'raspi', 'raspberry pi', 'saks'],
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Topic :: System :: Hardware :: Hardware Drivers',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'],
    install_requires = ['rpi.gpio'],
    license = 'GPL v2.0',
)
