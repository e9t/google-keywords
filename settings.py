#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
from time import strftime, localtime

HTMLPATH = 'data/google_blog_search/'
KEYWORDPATH = 'data/google_blog_search/'
NCRAWLPAGES = 100
#TODO: 한글 parsing 안 하도록
DELIMS = '[^\w\-]'
TREEDEPTH = 10
TODAY = strftime('%Y%m%d', localtime())
