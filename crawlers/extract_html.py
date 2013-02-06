#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os, re, json
import html5lib
from glob import glob
from pprint import pprint

import xpaths

def html_extractor(querylist, path, crawled_date):

    attrs = ['title', 'url', 'desc', 'page_no', 'crawled_time']

    queries = '_'.join(querylist)
    directory = '%s%s/' % (path, queries)
    files = get_file_list(directory, crawled_date)
    pprint([files[0], '...', files[-1]])

    pageno = 1
    extracted = []
    for f in files:
        print '%s%s%s' % ("extracting ", f, '...')
        #crawled_time = re.split('[\.\-]', f)[4]
        crawled_time = re.split('[\.\-]', f)[2]
        titles = extract_titles(f)
        urls = extract_urls(f)
        descs = extract_descriptions(f)
        for i in range(len(titles)):
            extracted.append(\
                    dict(zip(attrs,\
                        [titles[i], urls[i], descs[i], pageno, crawled_time])))
        pageno += 1
    
    filename = '%s%s-%s.%s' % (path, queries, crawled_date, 'json')
    with open(filename, 'w') as f:
        json.dump(extracted, f, indent=2)

def get_file_list(directory, matchstring):
    matchstring = '*%s*' % matchstring
    return glob(os.path.join(directory, matchstring))

def extract_titles(f):
    titles = []
    elements = parse_html(f, xpaths.google_search_title)
    for e in elements:
        tmp = e.xpath('a//text()')
        title = ''.join(tmp)
        titles.append(title)
    return titles

def extract_urls(f):
    def sanitize_url(e):
        e = e.strip("/url?q=")
        e = e.split('&sa=')[0]
        return e
    urls = []
    elements = parse_html(f, xpaths.google_search_url)
    elements = [sanitize_url(e) for e in elements]
    return elements

def extract_descriptions(f):
    descriptions = []
    elements = parse_html(f, xpaths.google_search_desc)
    for e in elements:
        tmp = e.xpath('text()')
        desc = ''.join(tmp)
        descriptions.append(desc)
    return descriptions

def parse_html(f, xpaths):
    with open(f, 'r') as F:
        x = get_xpaths(F, xpaths)
    return x

def get_xpaths(f, xpaths):
    p = html5lib.HTMLParser(\
        tree=html5lib.treebuilders.getTreeBuilder("lxml"),\
        namespaceHTMLElements=False)
    page = p.parse(f)
    xpaths = page.xpath(xpaths)
    return xpaths

if __name__ == '__main__':
    FILEPATH  = "../data/google_blog_search/"
    html_extractor([u'tv'], FILEPATH, '20120929')
