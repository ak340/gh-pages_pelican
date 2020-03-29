#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from markdown.extensions.codehilite import CodeHiliteExtension

AUTHOR = u'Aidyn Kemeldinov'
SITEURL = u'http://localhost:8000'
SITENAME = u"ak340"
SITETITLE = AUTHOR
EMPLOYERURL = "http://www.appliedmaterials.com"
EMPLOYERICON = "http://www.appliedmaterials.com/files/favicon_0.ico"
#CURRENTPLACE = '<a href="http://www.appliedmaterials.com/"><img src="http://www.appliedmaterials.com/files/favicon_0.ico"></a>'
CURRENTPLACE = '<a href="%s"><img src="%s" style="background-color:white"></a>'%(EMPLOYERURL,EMPLOYERICON)
SITESUBTITLE = 'Software Engineer at ' + CURRENTPLACE
SITEDESCRIPTION = u'cs physics audiobooks football and etc'
#BROWSER_COLOR = '#222222'
#PYGMENTS_STYLE = 'monokai'

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'
DATE_FORMATS = {
    'en': '%B %d, %Y',
}

USE_FOLDER_AS_CATEGORY = False
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10
LINKS_IN_NEW_TAB = False

# Theme Settings
SITELOGO = '/images/profile.jpg' #SITEURL + '/img/profile.png'
FAVICON = '/images/favicon.ico'
#THEME = 'Flex'
PYGMENTS_STYLE = 'default'


# Main Menu
MAIN_MENU = True
MENUITEMS = (('Archives', '/archives'),('Categories','/categories'),('Tags','/tags'),)

# Blogroll
#LINKS = (('About', '/pages/about'),)

# Social widget
SOCIAL = (('github', 'https://github.com/ak340'),
          ('linkedin', 'https://linkedin.com/in/aidynkemeldinov'),
          ('instagram', 'https://instagram.com/akemeldi'),
          )


CUSTOM_CSS = 'static/custom.css'
HOME_HIDE_TAGS = True
USE_LESS = False
FEED_USE_SUMMARY = True

# Formatting for URLS
ARTICLE_URL = 'posts/{slug}'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = 'pages/{slug}'
CATEGORY_URL = 'category/{slug}'
TAG_URL = 'tag/{slug}'


#

READERS = {'html': None}
FEED_ALL_ATOM = False


