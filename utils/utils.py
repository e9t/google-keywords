#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from collections import Counter

def flatten_list(listoflist):
    return [item for sublist in listoflist for item in sublist]

def word_counter(wordlist, nprint):
    cnt = _word_counter(wordlist)
    keywords = cnt.most_common(nprint)
    return keywords

def _word_counter(wordlist):
    cnt = Counter()
    for word in wordlist:
        cnt[word] += 1
    return cnt

def pprint_list(filename, data):
    with open(filename, 'w') as f:
        for d in data:
            f.write("%s,%d\n" % (d[0], d[1]))

def swap(a, b):
    return b, a
