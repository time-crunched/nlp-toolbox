import time
import os

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.conf import settings


from .forms import File_uploadForm
from .models import File_upload, SummaryRes

from sim_v1.textsummary import TEXTSummary
summary_document_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','sum_v1','upload')
#summary_document_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\sum_v1\upload'

summary_extraction_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'media','sum_v1','temp')
#summary_extraction_dir = r'C:\Users\ERDIG\Dropbox\Python\nlp_v1\media\sum_v1\temp'

summary_ratio = 0.01

class Upload(View):
    def post(self, request):
        time.sleep(1)  # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.

        form = File_uploadForm(self.request.POST, self.request.FILES)

        print(form.errors)

        if form.is_valid():

            document = form.save()
            data = {'is_valid': True, 'name': document.file.name, 'url': document.file.url}

        else:
            data = {'is_valid': False}

        return JsonResponse(data)

    def get(self, request):

        for document in File_upload.objects.all():
            document.file.delete()
            document.delete()

        doc_list = File_upload.objects.all()

        form = File_uploadForm()

        return render(self.request, 'upload.html', {'documents': doc_list, 'form': form,})

def sum_words(request):
    if request.method == 'POST':

        form = File_uploadForm(request.POST)

        if form.is_valid():
            form.save()
            sum_words = form.cleaned_data['sum_words']
            request.session['sum_words'] = sum_words

        else:
            pass
    else:
        pass

    return redirect('sum_v1:summarize')

def clear_database(request):
    for document in File_upload.objects.all():
        document.file.delete()
        document.delete()
    return redirect(request.POST.get('next'))

def Summarize(request):
    SummaryRes.objects.all().delete()

    summary_word_count = request.session['sum_words']

    for document in os.listdir(summary_document_dir):

        for filename in os.listdir(summary_extraction_dir):
            os.remove(os.path.join(summary_extraction_dir, filename))

        text_dir = os.path.join(summary_document_dir, document)

        summary = TEXTSummary(text_dir, summary_extraction_dir, summary_ratio, summary_word_count)
        summary.textextraction()
        summary.summary()

        SummaryRes.objects.create(doc = document, summary = summary.summary)

    results = SummaryRes.objects.all()

    return render(request, 'summarize.html', {'results': results})
