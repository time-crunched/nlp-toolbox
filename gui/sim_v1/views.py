import os
import glob
import pickle
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect

# import of classes for NLP:
from sim_v1.textsimilarity import TEXTSimilarity
from sim_v1.textsummary import TEXTSummary

# Directories:
query_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','sim_v1','upload')
#query_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\documents'

query_extraction_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','sim_v1','extraction')
#query_extraction_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\extraction'

summary_extraction_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','sim_v1','summary')
#summary_extraction_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\summary'

from .corpura_input import corpura_dict_dir  as corpura_dict_dir

#Summary
summary_ratio = 0.01
summary_word_count = 200

# Models

from .models import SimilarityRes

def calculate(request):

    with open(corpura_dict_dir , "rb") as fp:   #Pickling
        corpura_dict  = pickle.load(fp)

    corpus = request.session['corpus']
    query = TEXTSimilarity(corpura_dict[corpus]['corpus_mm_dir'],
    corpura_dict[corpus]['corpus_dict_dir'],
    query_dir, query_extraction_dir,
    corpura_dict[corpus]['corpus_doc_dict_dir'],
    corpura_dict[corpus]['language']
    )

    query.query_extraction()
    query.query_process()
    num_best = 5
    query.query_similarity(num_best)

    SimilarityRes.objects.all().delete()

    for i in range(0,num_best):
        sim_score, url = query.query_output(i)

        summary = TEXTSummary(url, summary_extraction_dir, summary_ratio, summary_word_count)
        summary.textextraction()
        summary.summary()

        SimilarityRes.objects.create(sim_score =  sim_score, url = url, summary = summary.summary)

    results = SimilarityRes.objects.all()
    query_doc = os.listdir(query_dir)[0]
    num_doc = corpura_dict[corpus]['num_doc']
    directory = corpura_dict[corpus]['search_dir']

    return render(request, 'sim_res.html', { 'results': results, 'query_doc': query_doc, 'num_best': num_best, 'num_doc': num_doc, 'directory': directory })

from .forms import DocumentForm

def model_form_upload(request):
    if request.method == 'POST':

        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            request.session['corpus'] = form.cleaned_data['directory']

            if form.cleaned_data['text_input'] == '':
                pass
            else:
                text_input = form.cleaned_data['text_input']
                outname = 'text_input'
                outfile = os.path.join(query_dir, outname+'.txt')
                output = open(outfile, 'wt', encoding = 'utf-8')
                output.write(str(text_input))
                output.close()

            return redirect('sim_v1:calculate')
    else:
        for filename in os.listdir(query_dir):
            os.remove(os.path.join(query_dir, filename))

        for filename in os.listdir(query_extraction_dir):
            os.remove(os.path.join(query_extraction_dir, filename))

        for filename in os.listdir(summary_extraction_dir):
            os.remove(os.path.join(summary_extraction_dir, filename))

        form = DocumentForm()

    return render(request, 'model_form_upload.html', {
        'form': form
    })
