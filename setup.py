from distutils.core import setup
version="0.1.1"
setup(
  name='friendpaste-api',
  packages=['friendpaste-api'],
  version=version,
  description='Simple Python API for friendpaste.com',
  author='Jorjon',
  author_email='jorjon@jorjon.com',
  url='https://github.com/Jorjon/friendpaste-api',
  download_url='https://github.com/Jorjon/friendpaste-api/archive/{0}.tar.gz'.format(version),
  keywords=['friendpaste', 'api', 'scrapper'],
  classifiers=[],
  license='MIT',
  install_requires=[
      'requests',
  ]
)