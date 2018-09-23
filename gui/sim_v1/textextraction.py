#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:35:22 2018

@author: Erik
"""
import os
import glob

class TEXTExtraction():
    '''This is a class containing methods for extraction of text from different kinds of documents'''

    def __init__(self, archive_dir, extraction_dir, docx, doc, pdf, txt):
        self.archive_dir = archive_dir
        self.extraction_dir = extraction_dir
        self.docxtextlist = []
        self.doctextlist = []
        self.pdftextlist = []
        self.txttextlist = []
        self.dict = {}
        self.docx = docx
        self.doc = doc
        self.pdf = pdf
        self.txt = txt

    def search(self):
        if self.docx == True:
            for docx_filename in glob.glob(os.path.join(self.archive_dir, '**/*.docx'), recursive = True):
                self.docxtextlist.append(docx_filename)
            print('The search found',len(self.docxtextlist),' .docx documents.')

        if self.doc == True:
            for doc_filename in glob.glob(os.path.join(self.archive_dir, '**/*.doc'), recursive = True):
                self.docxtextlist.append(doc_filename)
            print('The search found',len(self.doctextlist),' .doc documents.')

        if self.pdf == True:
            for pdf_filename in glob.glob(os.path.join(self.archive_dir, '**/*.pdf'), recursive = True):
                self.pdftextlist.append(pdf_filename)
            print('The search found',len(self.pdftextlist),' .pdf documents.')

        if self.txt == True:
            for txt_filename in glob.glob(os.path.join(self.archive_dir, '**/*.txt'), recursive = True):
                self.txttextlist.append(txt_filename)
            print('The search found',len(self.txttextlist),' .txt documents.')

        n = len(self.docxtextlist)+len(self.pdftextlist)+len(self.txttextlist)
        print('The search found in total',n,'documents in the directory:', self.archive_dir)


    def file2txt(self):
        docx_n = 0
        doc_n = 0
        pdf_n = 0
        txt_n = 0

        if self.docx == True:

            import docx2txt

            docx_fail = 0

            for filename in self.docxtextlist:
                try:
                    text = docx2txt.process(filename)
                    outname = 'docx'+str(docx_n)
                    outfile = os.path.join(self.extraction_dir, outname+'.txt')
                    output = open(outfile, 'wt', encoding = 'utf-8')
                    output.write(str(text))
                    docx_n = docx_n + 1
                    self.dict[outname] = filename
                    output.close()
                except:
                    print('It was not possible to extract text from',filename,'due to some error')
                    docx_fail = docx_fail + 1
                    pass
            print('Text was succesfully exctracted from',str(docx_n),'.docx documents. It failed extracting text from',str(docx_fail), '.docx documents.')

        if self.doc == True:
            import textract
            import chardet

            doc_fail = 0

            for filename in self.doctextlist:
                try:
                    text = textract.process(filename)
                    text = text.decode('utf-8')
                    print(str(text))
                    #print(chardet.detect(text))
                    outname = 'doc'+str(doc_n)
                    outfile = os.path.join(self.extraction_dir, outname+'.txt')
                    output = open(outfile, 'wt', encoding = 'utf-8')
                    output.write(str(text))
                    doc_n = doc_n + 1
                    self.dict[outname] = filename
                    output.close()
                except:
                    print('It was not possible to extract text from',filename,'due to some error')
                    doc_fail = doc_fail + 1
                    pass
            print('Text was succesfully exctracted from',str(doc_n),'.doc documents. It failed extracting text from',str(doc_fail), '.doc documents.')

        if self.pdf == True:
            import io
            from pdfminer.pdfinterp import PDFResourceManager, process_pdf
            from pdfminer.converter import TextConverter
            from pdfminer.layout import LAParams
            import logging

            pdf_fail = 0

            for filename in self.pdftextlist:
                try:
                    outname = 'pdf'+str(pdf_n)
                    logging.propagate = False
                    logging.getLogger().setLevel(logging.ERROR)
                    # input option
                    password = ''
                    pagenos = set()
                    maxpages = 0
                    # output option
                    outfile = os.path.join(self.extraction_dir, outname+'.txt')
                    caching = True
                    laparams = LAParams()
                    rsrcmgr = PDFResourceManager(caching=caching)
                    outfp = io.open(outfile, 'wt', encoding = 'utf-8', errors='ignore')
                    device = TextConverter(rsrcmgr, outfp, laparams=laparams)
                    fp = io.open(filename, 'rb')
                    process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages, password=password,
                                caching=caching, check_extractable=True)
                    pdf_n = pdf_n + 1
                    self.dict[outname] = filename
                    fp.close()
                    device.close()
                    outfp.close()
                except:
                    print('It was not possible to extract text from',filename,'due to some error')
                    pdf_fail = pdf_fail + 1
                    pass
            print('Text was succesfully exctracted from',str(pdf_n),'.pdf documents. It failed extracting text from',str(pdf_fail), '. pdf documents.')

        if self.txt == True:

            txt_fail = 0

            for filename in self.txttextlist:
                try:
                    file = open(filename, 'r')
                    text = file.read()
                    file.close()
                    outname = 'txt'+str(txt_n)
                    outfile = os.path.join(self.extraction_dir, outname+'.txt')
                    output = open(outfile, 'wt', encoding = 'utf-8')
                    output.write(str(text))
                    txt_n = txt_n + 1
                    self.dict[outname] = filename
                    output.close()
                    file.close()
                except:
                    print('It was not possible to extract text from',filename,'due to some error')
                    txt_fail = txt_fail + 1
                    pass
            print('Text was succesfully exctracted from',str(txt_n),'.txt documents. It failed extracting text from',str(txt_fail), '.txt documents.')

        self.num_doc = docx_n + doc_n + pdf_n + txt_n
