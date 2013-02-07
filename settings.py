#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from time import strftime, localtime

TARGET = 'news'                                 # Either 'news' or 'blog'
QUERYLIST = ['data', 'mining']                  # Enter list of queries
HTMLPATH = 'data/html/'                         # Paths should end with a slash ('/')
KEYWORDPATH = 'data/keywords/'
NCRAWLPAGES = 3                                 # Range: [1, 100]
DELIMS = '[^\w\-]'                              # TODO(lucypark): 한글 parsing 안 하도록
TODAY = strftime('%Y%m%d', localtime())
