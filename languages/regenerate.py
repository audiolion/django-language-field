#!/usr/bin/env python
"""
To regenerate that module to contain the latest list of  IANA Language
Subtag Registry, either call this module directly from the command line
(``python regenenerate.py``), or call the ``regenerate`` method.

"""
import os
import re
import codecs
import urllib2

TEMPLATE = u'''# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    %(languages)s
)

'''

def regenerate(location='http://www.iana.org/assignments/language-subtag-registry',
               filename=None, default_encoding='utf-8'):
    """
    Generate the languages Python module.
    """
    paren = re.compile('\([^)]*\)')

    # Get the language list.
    data = urllib2.urlopen(location)
    if ('content-type' in data.headers and
                'charset=' in data.headers['content-type']):
        encoding = data.headers['content-type'].split('charset=')[-1]
    else:
        encoding = default_encoding
    content = data.read().decode(encoding)
    languages = []
    info = {}
    p = None
    for line in content.splitlines():
        if line == '%%':
            if 'Type' in info and info['Type'] == 'language':
                languages.append(info)
            info = {}
        elif ':' not in line and p:
            info[p[0]] = paren.sub('', p[2]+line).strip()
        else:
            p = line.partition(':')
            if not p[0] in info: # Keep the first description as it should be the most common
                info[p[0]] = paren.sub('', p[2]).strip()

    languages_lines = map(lambda x:'("%s", _(u"%s")),'%(x['Subtag'],x['Description']), languages)

    # Generate and save the file.
    if not filename:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'languages.py')
    # TODO: first make a backup of the file if it exists already.
    f = codecs.open(filename, 'w', 'utf-8')
    f.write(TEMPLATE % {
        'languages': '\n    '.join(languages_lines),
    })
    f.close()

if __name__ == '__main__':
    regenerate()
