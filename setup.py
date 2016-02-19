from distutils.core import setup
setup(
  name = 'logiy',
  packages = ['logiy'], # this must be the same as the name above
  version = '0.2',
  install_requires=[
    'python-dateutil',
  ],
  description = 'Logiy is simple logging library to print a log in your python command.',
  author = 'Frans Siswanto',
  author_email = 'franssiswanto@gmail.com',
  url = 'https://github.com/franziz/logiy', # use the URL to the github repo
  download_url = 'https://github.com/franziz/logiy/tarball/0.2', # I'll explain this in a second
  keywords = ['logging', 'logiy'], # arbitrary keywords
  classifiers=[
    'Programming Language :: Python :: 2',
    'Natural Language :: English',
    'Intended Audience :: Developers',
  ],
)