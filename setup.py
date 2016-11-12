from distutils.core import setup
setup(
  name = 'django-language-field',
  packages = ['django-language-field'], # this must be the same as the name above
  version = __version__,
  description = 'A pluggable django app that provides a comprehensive language choices field',
  author = 'Ryan Castner',
  author_email = 'ryancastner@gmail.com',
  url = 'https://github.com/audiolion/django-language-field', # use the URL to the github repo
  keywords = ['django','language','languages','field'], # arbitrary keywords
  classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
)
