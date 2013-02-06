#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import nltk
import json, os
from pprint import pprint
from glob import glob
import operator

from nlp import parser, rm_stopwords, list_filter
from utils import word_counter
import config

def get_keywords(querylist, delims, input_path, output_path, crawled_date):
    # nltk.data.path.append('/Users/lucypark/data/nltk_data')
    # TODO: 한글로 parsing 안되게 고치기
    # TODO: unicode 지원
    # TODO: check collocations

    queries = '_'.join(querylist)

    inp = input_filename(queries, crawled_date)
    filenames = get_filenames(input_path, inp)
    pprint(filenames)

    # TODO: why search _results[0]?
    with open(filenames[0], 'r') as f:
        docs = json.load(f)

    # TODO: d['title']로 출력했더니 같은 entry가 계속 나옴, 버그있는듯
    text = ''
    for d in docs:
        text = text + d['title']

    parsed = parser(text, delims)
    sanitized = [sanitizer(p) for p in parsed]
    # stems = stemmer(removed)
    removed = rm_stopwords(sanitized)
    filtered = filter(None, removed)

    keywords = word_counter(filtered, config.NKEYWORDS)

    '''
    d = dict()
    for k in keywords:
        d[k[0]] = k[1]

    sorted_d = sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)
    pprint(sorted_d[0:config.NPRINTWORDS])
    '''
    pprint(keywords[0:config.NPRINTWORDS])

    outp = output_filename(queries)
    with open(output_path + outp, 'w') as f:
        # json.dump(d, f, indent=2)
        for k in keywords:
            json.dump(k, f)
            f.write(',\n')

    # TODO: keyword 결과에 tag까지 붙도록
    '''
    tags = dict(nltk.pos_tag(filtered))
    keyword_tags = [tags[k[0]] for k in keywords]
    kt = zip(keywords, keyword_tags)
    pprint(kt)
    return kt
    '''
    return keywords

def input_filename(queries, crawled_date):
    return '%s-%s%s' % (queries, crawled_date, '*.json')

def output_filename(queries):
    return '%s-%s.%s' % ('keywords', queries, 'json')

def get_titles(json):
    titles = ''
    for d in json:
        titles = titles + d['title']
    return titles

def get_descs(json):
    descs = ''
    for d in json:
        descs = descs + d['desc']
    return descs

def sanitizer(text):
    text = text.replace('-','')
    text = text.lower()
    return text

def get_filenames(directory, matchstring):
    return glob(os.path.join(directory, matchstring))

if __name__ == '__main__':

    settings = {
        'GETPATH': "data/google_news_search/html/",
        'PUTPATH': "data/google_news_search/keywords/",
        'DELIMS': '[^\w\-]',
        'CRAWLEDDATE': '20130112',
    }

    import sys
    if len(sys.argv) > 1:
        get_keywords(sys.argv[1:],\
                settings['DELIMS'], settings['GETPATH'], settings['PUTPATH'],\
                settings['CRAWLEDDATE'])
    else:
        get_keywords(['Google TV'],\
                settings['DELIMS'], settings['GETPATH'], settings['PUTPATH'],\
                settings['CRAWLEDDATE'])
