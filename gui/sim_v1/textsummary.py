#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  3 13:15:29 2018

@author: Erik
"""
from sim_v1.textextraction import TEXTExtraction
from gensim.summarization.summarizer import summarize
import glob
import os

class TEXTSummary():
    'This class contains methods for summarization of text'

    def __init__(self, text_dir, summary_extraction_dir, ratio, word_count):
        self.text_dir = text_dir
        self.summary_extraction_dir = summary_extraction_dir
        self.ratio = ratio
        self.word_count = word_count
        self.docx = True
        self.doc = True
        self.pdf = True
        self.txt = True

    def textextraction(self):
        self.text_extraction = TEXTExtraction(self.text_dir, self.summary_extraction_dir, self.docx, self.doc, self.pdf, self.txt)
        if os.path.splitext(self.text_dir)[1] == '.docx':
            self.text_extraction.docxtextlist.append(self.text_dir)

        if os.path.splitext(self.text_dir)[1] == '.doc':
            self.text_extraction.doctextlist.append(self.text_dir)

        elif os.path.splitext(self.text_dir)[1] == '.pdf':
            self.text_extraction.pdftextlist.append(self.text_dir)

        elif os.path.splitext(self.text_dir)[1] == '.txt':
            self.text_extraction.txttextlist.append(self.text_dir)

        self.text_extraction.file2txt()

    def summary(self):
        filename = glob.glob(os.path.join(self.summary_extraction_dir, '*.txt'))[0]
        with open(filename,'r', encoding = 'utf-8') as f:
            self.text = f.read()
            self.summary = summarize(self.text, ratio = self.ratio, word_count = self.word_count)
