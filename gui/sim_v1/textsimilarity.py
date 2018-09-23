#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:59:46 2018

@author: Erik
"""
from .textextraction import TEXTExtraction
from .textprocess import TEXTProcess
from gensim import corpora
from gensim import models
from gensim import similarities
import numpy as np
import pickle

class TEXTSimilarity():
    '''This is a class containing methods calculation of semantic similarity'''
    
    def __init__(self,corpus_dir, dictionary_dir, query_dir, query_extraction_dir, corpus_doc_dict_dir, language):
        self.corpus_dir = corpus_dir
        self.dictionary_dir = dictionary_dir
        self.query_dir = query_dir
        #self.archive_dict_dir = archive_dict_dir
        self.archive_dict = {}
        self.query_extraction_dir = query_extraction_dir
        self.corpus_doc_dict_dir = corpus_doc_dict_dir
        self.language = language
        self.docx = True
        self.doc = True
        self.pdf = True
        self.txt = True
        
    def query_extraction(self):
        self.query_extraction = TEXTExtraction(self.query_dir, self.query_extraction_dir, self.docx, self.doc, self.pdf, self.txt)
        self.query_extraction.search()
        self.query_extraction.file2txt()
    
    def query_process(self):
        self.query_process = TEXTProcess(self.query_extraction_dir, self.dictionary_dir, self.archive_dict, self.language)
        self.query_process.tokenizer()
        self.query_process.txtfilter()
        self.query_process.stemmer()

        #with open(self.archive_dict_dir,'rb') as fp:
            #self.archive_dict = pickle.load(fp)
            
        self.query_doc_bow = self.query_process.corpus()
        
    def query_similarity(self, num_best):
        self.num_best = num_best
        self.corpus = corpora.MmCorpus(self.corpus_dir)
        self.dictionary = corpora.Dictionary.load(self.dictionary_dir)
        
        self.tfidf = models.TfidfModel(self.corpus) #Training of a TF-IDF model from the documents in the corpus
        
        self.corpus_tfidf = self.tfidf[self.corpus] #Transformation of the whole corpus according to the TF-IDF modell
        self.query_tfidf = self.tfidf[self.query_doc_bow]
        
        
        self.lsi = models.LsiModel(self.corpus_tfidf, id2word=self.dictionary, num_topics=300) # initialize an LSI transformation
        
        self.corpus_lsi = self.lsi[self.corpus_tfidf] #Double transformation of corpus: Corpus -> TF-IDF -> LSI        
        self.query_lsi = self.lsi[self.query_tfidf]
        
        self.index = similarities.Similarity(self.query_extraction_dir, self.corpus_lsi, num_features = len(self.dictionary), num_best = self.num_best)

        self.similarity = self.index[self.query_lsi]
    
    def query_output(self, nr):    
        with open(self.corpus_doc_dict_dir, 'rb') as fp:
            self.corpus_doc_dict = pickle.load(fp)
        
        self.sim_ind = self.similarity[0][nr][0]
        self.docurl = self.corpus_doc_dict[self.sim_ind]
        
        
        self.sim_score = self.similarity[0][nr][1]
        
        return self.sim_score, self.docurl