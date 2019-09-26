#!/usr/bin/env python
"""
To regenerate that module to contain the latest list of  IANA Language
Subtag Registry, either call this module directly from the command line
(``python regenenerate.py``), or call the ``regenerate`` method.

"""
import os
import re
import codecs
import urllib.request

LANGUAGES_TEMPLATE = u'''# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    %(languages)s
)

'''

REGIONS_TEMPLATE = u'''# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

REGIONS = (
    %(regions)s
)

'''

location='http://www.iana.org/assignments/language-subtag-registry'

def regenerate(filename=None, encoding='utf-8'):
    """
    Generate the languages Python module.
    """
    paren = re.compile('\([^)]*\)')

    # Get the language list.
    data = urllib.request.urlopen(location)
    if 'content-type' in data.headers and 'charset=' in data.headers['content-type']:
        encoding = data.headers['content-type'].split('=')[1].lower()
    languages = []
    regions = []
    info = {}
    p = None
    for line in data.read().decode(encoding).splitlines():
        if line == '%%':
            if 'Type' in info:
                if info['Type'] == 'language':
                    languages.append(info)
                elif info['Type'] == 'region':
                    regions.append(info)
            info = {}
        elif ':' not in line and p:
            info[p[0]] = paren.sub('', p[1]+line).strip()
        else:
            p = line.split(':')
            if not p[0] in info:  # Keep the first description as it should be the most common
                info[p[0]] = paren.sub('', p[1]).strip()

    languages_lines = map(lambda x: '("%s", _(u"%s")),' % (x['Subtag'], x['Description']), languages)
    regions_lines = map(lambda x: '("%s", _(u"%s")),' % (x['Subtag'], x['Description']), regions)

    # Generate and save the file.
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'languages.py'), 'w', encoding='utf-8') as f:
        f.write(LANGUAGES_TEMPLATE % {
            'languages': '\n\t'.join(languages_lines),
        })

    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'regions.py'), 'w', encoding='utf-8') as f:
        f.write(REGIONS_TEMPLATE % {
            'regions': '\n\t'.join(regions_lines),
        })


if __name__ == '__main__':
    regenerate()
