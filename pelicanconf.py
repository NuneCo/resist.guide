#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic site information
AUTHOR = 'resist.guide'
SITETITLE = AUTHOR
SITESUBTITLE = 'resist.guide encourages hindsight'
SITEDESCRIPTION = '...it is 2020 after all.'
SITENAME = 'resist.guide'
SITEURL = 'https://resist.guide'

# UI settings
THEME = 'theme/flex'
DEFAULT_LANG = 'en'
BROWSER_COLOR = '#333333'
DEFAULT_PAGINATION = 13
USE_LESS = True

# OpenGraph
OG_LOCALE = 'en_US'
OG_IMAGE = SITEURL + '/solidarity.png'

# Time and date
TIMEZONE = 'America/Los_Angeles'
DATE_FORMATS = {
    'en': '%c',
}

# Disable feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Site Navigation Settings
DISPLAY_PAGES_ON_MENU = True
DEFAULT_PAGINATION = 13
SOCIAL = (
    ('github', 'https://github.com/resist-guide/resist.guide/'),
    ('twitter', 'https://twitter.com/jakimfett'),
)
LINKS = (
    ('Contribute', 'https://github.com/resist-guide/resist.guide'),
)

# Legal
COPYRIGHT_YEAR = 2017
CC_LICENSE = {
    'name': 'Creative Commons Attribution-NonCommercial-ShareAlike International',
    'version': '4.0',
    'slug': 'by-nc-sa'
}


# Files
PATH = 'content'
SITELOGO = SITEURL + '/logo.svg'
FAVICON = SITEURL + '/favicon.ico'
ROBOTS = 'index, follow'

# Static path settings
STATIC_PATHS = [
    'extra/logo.svg',
    'extra/logo_og.png',
    'extra/favicon.ico',
    'extra/CNAME',
]

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'},
    'extra/logo_og.png': {'path': 'logo_og.png'},
}
