import io
import os
from distutils.core import setup


version="0.1.9.2"

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

setup(
  name='friendpaste-api',
  packages=['friendpaste-api'],
  version=version,
  description='Simple Python API for friendpaste.com',
  long_description=long_description,
  author='Jorjon',
  author_email='jorjon@jorjon.com',
  url='https://github.com/Jorjon/friendpaste-api',
  # download_url='https://github.com/Jorjon/friendpaste-api/archive/{0}.tar.gz'.format(version),
  keywords=['friendpaste', 'api', 'scrapper'],
  classifiers=[],
  license='MIT',
  install_requires=[
      'requests',
  ]
)