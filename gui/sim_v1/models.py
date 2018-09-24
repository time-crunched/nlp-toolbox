from django.db import models
from django import forms
import pickle

from .corpura_input import corpura_dict_dir  as corpura_dict_dir

class Document(models.Model):

    text_input = models.TextField(blank = True)

    document = models.FileField(upload_to='sim_v1/upload/', blank = True)

    with open(corpura_dict_dir , "rb") as fp:   #Pickling
        corpura_dict  = pickle.load(fp)

    corpus_choices = ()

    for corpus in corpura_dict:
        choice = (corpus, corpura_dict[corpus]['search_dir'])
        corpus_choices = corpus_choices + (choice,)

    directory = models.CharField(max_length = 200, choices = corpus_choices, default = '/Users/Erik/Documents/Python/NLP/Extraction/Corpus/corpus.mm',)

class SimilarityRes(models.Model):
    sim_score = models.DecimalField(decimal_places = 2, max_digits = 4)
    url = models.URLField()
    summary = models.TextField()

    def __str__(self):
           return self.url
