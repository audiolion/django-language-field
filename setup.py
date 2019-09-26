import os

from setuptools import setup, find_packages
import languages as app

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
  name = 'django-language-code-fields',
  version = app.__version__,
  description = 'A pluggable django app that provides a comprehensive language and region choices field',
  long_description=read('README.rst'),
  author='Ryan Castner',
  author_email='ryancastner@gmail.com',
  url = 'https://github.com/Coykto/django-language-field', # use the URL to the github repo
  license='MIT',
  platforms=['OS Independent'],
  packages = ['languages'], # this must be the same as the name above
  zip_safe=False,
  keywords = ['django','language','languages','field'], # arbitrary keywords
  classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)
