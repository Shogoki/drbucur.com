#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dr. Viorel Bucur'
SITENAME = u'Dr. Bucur'
SITEURL = ''
THEME = '/home/ec2-user/pelican0/theme/pelican-bootstrap3'
PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'de'

DEVELOPER = 'Sven Kraus'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['/home/ec2-user/pelican0/pelican-plugins', ]
PLUGINS = ['i18n_subsites', 'thumbnailer']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

##Thumbnailer config
IMAGE_PATH = 'content/images/'
THUMBNAIL_DIR = 'content/thumbs/'
THUMBNAIL_SIZES = {'medium':'500x?'}
THUMBNAIL_KEEP_NAME = False;
THUMBNAIL_KEEP_TREE = False;

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## TEMPLATE VARS
#SITELOGO = 'images/stetoskop.png'
#SITELOGO_SIZE = 40
HIDE_SITENAME = True
BANNER = 'images/left_banner.png'
#BOOTSTRAP_NAVBAR_INVERSE = Truea
FAVICON = 'images/favicon.ico'
#SOCIAL = ()
BANNER_ALL_PAGES= True
HIDE_SIDEBAR = True
PAGES_SORT_ATTRIBUTE = 'pageorder'
