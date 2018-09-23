#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:48:20 2018

@author: Erik
"""
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from string import punctuation
import glob
import os
from gensim import corpora
from six import iteritems

def listgen(filename):
    txtlist = []
    with open(filename,'r') as f:
            for line in f:
                txtlist.append(line.rstrip())
    return txtlist

class TEXTProcess():
    '''This is a class containing methods for processing of text.'''
    
    def __init__(self, extraction_dir, dictionary_dir, archive_dict, language):
        self.extraction_dir = extraction_dir
        self.dictionary_dir = dictionary_dir
        self.archive_dict = archive_dict
        self.language = language
        #self.corpus_index = []
        
    
    def tokenizer(self):     
        for filename in glob.glob(os.path.join(self.extraction_dir, '*.txt')):
            with open(filename,'r') as f:
                text = f.read()
                text = word_tokenize(text)
            
            with open(filename,'w') as f:
                for word in text:
                    word = word.lower()
                    f.write("%s\n" % word)
    
    
    def txtfilter(self):
        for filename in glob.glob(os.path.join(self.extraction_dir, '*.txt')):
            text = listgen(filename)
            
            stopwords_lang = set(stopwords.words(self.language)) #Set med stop ord
            
            text = [word for word in text if word not in stopwords_lang] #Sletting av stop ord i importert tekst
            text = [word for word in text if word not in punctuation] #Sletting av punktum, komma, utropstegn etc. i importert tekst
            
            with open(filename,'w') as f:
                for word in text:
                    f.write("%s\n" % word)
    
    def stemmer(self):
        for filename in glob.glob(os.path.join(self.extraction_dir, '*.txt')):
            text = listgen(filename)
            
            snowball = SnowballStemmer(self.language)
            text = [snowball.stem(word) for word in text]
            
            with open(filename,'w') as f:
                for word in text:
                    f.write("%s\n" % word)
                    
    def dictionary(self):

        self.dictionary = corpora.Dictionary(listgen(filename) for filename in glob.glob(os.path.join(self.extraction_dir, '*.txt')))
        once_ids = [tokenid for tokenid, docfreq in iteritems(self.dictionary.dfs) if docfreq == 1]
        self.dictionary.filter_tokens(once_ids)  # remove stop words and words that appear only once
        self.dictionary.compactify()  # remove gaps in id sequence after words that were removed
        return self.dictionary
    
    def corpus(self):
        
        self.corpus_doc_dict = {}
        n = 0
        
        self.dictionary = corpora.Dictionary.load(self.dictionary_dir)
        
        for filename in glob.glob(os.path.join(self.extraction_dir, '*.txt')):
            
            #self.corpus_index.append(os.path.splitext(os.path.basename(filename))[0])
            try:
                docname = os.path.splitext(os.path.basename(filename))[0]
                #print(docname)
                #print(self.archive_dict[docname])
            
                self.corpus_doc_dict[n] = self.archive_dict[docname]
                n = n + 1
                
            except:
                pass
            
            yield self.dictionary.doc2bow(listgen(filename))