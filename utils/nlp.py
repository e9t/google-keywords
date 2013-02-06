#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import re
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#from crawler import search_blogs

def parser(text, delims):
    return re.split(delims, text)

def encoder(parsed_text):
    return [line.encode('utf-8') for line in parsed_text]

def stemmer(encoded_parsed_text):
    st = PorterStemmer()
    return [st.stem(word) for word in encoded_parsed_text]

def rm_stopwords(wordlist):
    return [w for w in wordlist if not w in stopwords.words('english')] 

def list_filter(wordlist):
    return list(filter(None, wordlist))

if __name__ == '__main__':
    DELIMS = '[^\w\-]'

    #text = search_blogs('smart+tv', 1) 
    #text = stemmer(text, DELIMS)
    #print text
