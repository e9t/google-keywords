#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys

import settings
from crawlers.crawler import crawler
from utils.keywords import get_keywords

if len(sys.argv) > 1:
    querylist = sys.argv[1:]
else:
    querylist = settings.QUERYLIST

# Scrape and parse search results from Google, and save in json format
crawler(settings.TARGET, querylist, settings.HTMLPATH, settings.NCRAWLPAGES)

# Calculate frequent words from search results
get_keywords(querylist, settings.DELIMS,
        input_path=settings.HTMLPATH,
        output_path=settings.KEYWORDPATH,
        crawled_date=settings.TODAY)
