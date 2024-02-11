#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Amadeus Gebauer'
SITENAME = 'Übersicht'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (('DAV USC München', 'https://www.dav-usc-muenchen.de/'),
         ('Alpenvereinaktiv.com', 'https://www.alpenvereinaktiv.com/'))

STATIC_PATHS = ['images']

THEME = "themes/medius"

# Medius config
MEDIUS_CATEGORIES = {
    'Tipps & Tricks': {
        'description': 'Wenn man ein paar Dinge beachtet kommt man entspannt mit der Bahn in die Berge und wieder zurück. Hier findest du wichtige Tipps.',
        'thumbnail': 'images/kleiner_zug.jpeg'
    },
    'Touren': {
        'description': 'Eine kleine Sammlung von Touren mit öffentlicher Anreise.',
        'thumbnail': 'images/gipfelkreuz.jpeg'
    }
}


MEDIUS_AUTHORS = {
    'Amadeus Gebauer': {
        'description': """
            Ich bin sehr oft in den Bergen unterwegs und mache fast alle meine Skitouren, Hochtouren, Klettertouren und Mountainbiketouren mit den öffentlichen Verkehrsmitteln.
        """,
        'cover': 'images/amadeus_cover.jpeg',
        'image': 'images/amadeus_gebauer_small.jpeg',
        'links': (),
    }
}