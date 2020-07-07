import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'iotdatalog',
  packages = ['iotdatalog'],
  version = '0.1',
  license='GPLv3',
  description = 'Wrapper for datalog.anglebrackets.co.za REST API',
  author = 'Ruan Luies',
  author_email = 'omega@live.co.za',
  url = 'https://github.com/baggins800/iotdatalog',
  download_url = 'https://github.com/baggins800/iotdatalog/archive/v_01.tar.gz',
  keywords = ['IOT', 'datalogging', 'datalog', 'datalogger'],
  install_requires=[  
    'requests>=1.6', 'responses'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GPLv3',
  ],
)
