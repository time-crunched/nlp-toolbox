#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 09:16:00 2018

@author: Erik
"""

from textextraction import TEXTExtraction
from textprocess import TEXTProcess
from gensim import corpora
import pickle
import os, shutil

from corpura_input import corpura_dict as corpura_dict
from corpura_input import corpura_dir  as corpura_dir
from corpura_input import corpura_dict_dir  as corpura_dict_dir

for corpus in corpura_dict:
    
    corpus_dir = os.path.join(corpura_dir,corpus)
    
    if os.path.exists(corpus_dir):
        for filename in os.listdir(corpus_dir):
            filepath = os.path.join(corpus_dir, filename)
            
            try:
                if os.path.isfile(filepath):
                    os.unlink(filepath)
                    
                elif os.path.isdir(filepath): 
                    shutil.rmtree(filepath)
                    
            except Exception as e:
                print(e)
    else:    
        os.makedirs(corpus_dir)
    
    corpura_dict[corpus]['corpus_dir'] = corpus_dir
    
    temp_dir = os.path.join(corpus_dir,'temp')
    
    if os.path.exists(temp_dir):
        try:
            shutil.rmtree(temp_dir)
        
        except:
            pass
    else:
        os.makedirs(temp_dir)
    
    archive_extraction = TEXTExtraction(corpura_dict[corpus]['search_dir'],
                                        temp_dir,
                                        corpura_dict[corpus]['docx'],
                                        corpura_dict[corpus]['doc'],
                                        corpura_dict[corpus]['pdf'],
                                        corpura_dict[corpus]['txt']
                                        )

    archive_extraction.search()
    archive_extraction.file2txt()
    corpura_dict[corpus]['num_doc'] = archive_extraction.num_doc
    
    archive_dict_dir = os.path.join(corpus_dir,'archive_dictionary.p')
    corpura_dict[corpus]['archive_dict_dir'] = archive_dict_dir
    archive_dict = archive_extraction.dict
    with open(archive_dict_dir, "wb") as fp:   #Save archive_dict on disk for later use
        pickle.dump(archive_dict, fp)
   
    
    #archive_index_dir = os.path.join(corpus_dir,'archive_index.p')
    #corpura_dict[corpus]['archive_index_dir'] = archive_index_dir
    #archive_index = archive_extraction.index

    #with open(archive_index_dir, "wb") as fp:   #Save archive_index on disk for later use
        #pickle.dump(archive_index, fp)

    corpus_dict_dir = os.path.join(corpus_dir,'dictionary.dict')
    corpura_dict[corpus]['corpus_dict_dir'] = corpus_dict_dir
    
    archive_process = TEXTProcess(temp_dir, corpus_dict_dir, archive_dict, corpura_dict[corpus]['language'])
    archive_process.tokenizer()
    archive_process.txtfilter()
    archive_process.stemmer()
    dictionary = archive_process.dictionary()
    dictionary.save(corpus_dict_dir)
    corpus_mm_dir = os.path.join(corpus_dir,'corpus.mm')
    corpura_dict[corpus]['corpus_mm_dir'] = corpus_mm_dir
    corpora.MmCorpus.serialize(corpus_mm_dir, archive_process.corpus(), metadata = True)  # store to disk, for later use
    
    corpus_doc_dict_dir = os.path.join(corpus_dir,'corpus_doc_dict.p')
    corpura_dict[corpus]['corpus_doc_dict_dir'] = corpus_doc_dict_dir
    
    with open(corpus_doc_dict_dir, "wb") as fp:
        pickle.dump(archive_process.corpus_doc_dict, fp)   
 
    #corpus_doc_index_dir = os.path.join(corpus_dir,'corpus_doc_index.p')
    #corpura_dict[corpus]['corpus_doc_index_dir'] = corpus_doc_index_dir
    #with open(corpus_doc_index_dir, "wb") as fp:
        #pickle.dump(archive_process.corpus_index, fp)

with open(corpura_dict_dir, 'wb') as fp:
    pickle.dump(corpura_dict, fp)