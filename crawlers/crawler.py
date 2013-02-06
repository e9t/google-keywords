#! /usr/bin/python
# -*- coding: utf-8 -*-

import get_html
import extract_html
from time import strftime, localtime

def crawler(querylist):
    path = 'data/html/google_news_search/'
    npages = 100

    print '---Crawling-----'
    get_html.search_google('news', querylist, npages, path)


    print '---Extracting-----'
    today = strftime('%Y%m%d', localtime())
    extract_html.html_extractor(querylist, path, today)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        # TODO: unicode 지원
        querylist = sys.argv[1:]
    else:
        querylist = [u'tv contents']
    crawler(querylist)
