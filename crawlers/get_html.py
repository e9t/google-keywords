#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import os, urllib2
from time import strftime, localtime

def search_google(searchtype, querylist, npages, savepath):

    if searchtype == 'blogs':
        metainfo = get_google_blogs_metainfo()
    elif searchtype == 'news':
        metainfo = get_google_news_metainfo()
    else:
        raise Exception("nah... wrong type of search.")

    querylist = encode_queries(querylist) 
    query = querylist2query(querylist)
    base_url = metainfo['base_url'] + query + '''&start='''

    for i in range(npages):
        url = base_url + str(i * 10 + 1) 
        print 'retrieving ' + url + '...'

        [pname, fname] = querylist2filename(savepath, querylist,'p'+str(i+1), 'html')
        f = get_html_tree(url)

        if not os.path.exists(pname):
            os.makedirs(pname)

        html2file(pname+fname, f)

def encode_queries(querylist):
    return [q.encode('utf-8') for q in querylist] 

def get_google_blogs_metainfo():
    metainfo = {"type": 'google_blog_search',
            "base_url": "https://www.google.com/search?hl=en&tbm=blg&q="
            }
    return metainfo 

def get_google_news_metainfo():
    metainfo = {"type": 'google_news_search',
            "base_url": "https://www.google.com/search?hl=en&tbm=nws&q="
            }
    return metainfo 
    
def querylist2query(querylist):
    querylist = ['%s%s%s' % ('%22', q.replace(' ','+'), '%22')\
                for q in querylist]
    query = '%2C'.join(querylist)
    return query

def querylist2filename(path, querylist, pageno, ext):
    # querylist = [q.replace(' ','-') for q in querylist]
    queries = '_'.join(querylist)
    t = strftime("%Y%m%d_%H%M%S", localtime())
    pname = '%s/%s/' % (path, queries)
    fname = '%s-%s-%s.%s' % (queries, pageno, t, ext)
    return [pname, fname]

def get_html_tree(url):
    r = urllib2.Request(url)
    r.add_header("User-Agent", "Mozilla/5.0")
    f = urllib2.urlopen(r)
    return f

def html2file(filename, html):
    with open(filename, 'w') as f:
        f.write(html.read())

if __name__ == '__main__':
    SEARCHTYPE  = 'blogs'
    QUERYLIST   = [u'tv', u'스마트', u'lg']
    NPAGES      = 100
    SAVEPATH    = '../data/google_blog_search'

    search_google(SEARCHTYPE, QUERYLIST, NPAGES, SAVEPATH)
